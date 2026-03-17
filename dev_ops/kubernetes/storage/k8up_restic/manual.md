# K8up Operations Manual

## K8up CR Model

K8up splits backup configuration across multiple Custom Resources:

- **PreBackupPod** — defines **what** to back up and **how** (image, commands, credentials, volumes). Stays in the cluster permanently.
- **Schedule** — defines **when** backups run (cron expressions, retention rules). Creates Backup/Prune/Check CRs automatically on schedule.
- **Backup** — a single backup run. Created automatically by a Schedule, or manually by an admin. Discovers all PreBackupPods in its namespace and executes them.
- **Snapshot** — represents the actual data stored in S3. One Backup creates one Snapshot per source (per PVC, per PreBackupPod).

So to set up backups: create a PreBackupPod (how) and a Schedule (when). To trigger a one-off: create a Backup CR — it picks up the existing PreBackupPod automatically.

---

## Restic Access

K8up stores all backups in a Restic repository on S3. Some operations (like deleting a specific backup) require direct restic CLI access. There are two ways:

### Option A: Exec into the Operator Pod

Temporarily Increase Operator Memory
```bash
kubectl set resources -n k8up-system deploy/k8up --limits=memory=2Gi
# ... do your work ...
kubectl set resources -n k8up-system deploy/k8up --limits=memory=256Mi  # restore original
```
⚠️ This restarts the operator pod.

```bash
kubectl exec -it -n k8up-system deploy/k8up -- sh
```

⚠️ Remember to decrease the memory limit after your work on the operator pod.

### Option B: Temporary Interactive Pod

For operations that need more memory (e.g. prune on large repos) or interactive CLI work:

```bash
kubectl run restic-cli --rm -it \
  --image=ghcr.io/k8up-io/k8up:v2.13.1 \
  --namespace=k8up-system \
  --overrides='{
    "spec": {"containers": [{"name": "restic-cli", "image": "ghcr.io/k8up-io/k8up:v2.13.1",
      "stdin": true, "tty": true, "command": ["sh"],
      "resources": {"limits": {"memory": "1Gi"}}}]}
  }' -- sh
```

Then set this env vars:
```bash
export RESTIC_REPOSITORY=s3:s3.amazonaws.com/<bucket>
export RESTIC_PASSWORD=<repo-password>
export AWS_ACCESS_KEY_ID=<key>
export AWS_SECRET_ACCESS_KEY=<secret>
```

---

## Listing Backups

### Via Kubernetes

K8up has two relevant CRs:

- **Backup CR** — the job that triggered the backup run: `kubectl get backups -n my-app`
- **Snapshot CR** — the actual data stored in S3. One Backup creates one Snapshot per source (per PVC, per PreBackupPod): `kubectl get snapshots -n my-app`

To see what data you have, list Snapshots. To see backup job history, list Backups.

### Via Restic

More powerful filtering:

```bash
# All backups, grouped by source
restic snapshots --group-by path

# Filter by app (path = PreBackupPod CR name + .spec.fileExtension)
restic snapshots --path /my-app-backup.tar

# Filter by namespace (K8up sets hostname = namespace)
restic snapshots --host my-app

# Filter by tag
restic snapshots --tag prod
```

---

## Creating a Manual Backup

Create a one-off Backup CR. It discovers and runs **all** (⚠️) PreBackupPods in the namespace:

```yaml
apiVersion: k8up.io/v1
kind: Backup
metadata:
  name: manual-backup
  namespace: my-app
spec:
  tags:
    - manual
```

```bash
kubectl apply -f manual-backup.yaml

# Watch progress
kubectl get backups -n my-app -w

# Check logs
kubectl logs -n my-app -l k8up.io/owned-by=backup_manual-backup
```

The Backup CR and its Job are cleaned up automatically based on Schedule history limits.

---

## Deleting a Specific Backup

K8up has no CR for selective deletion. This requires restic directly:

```bash
# 1. Find the backup (snapshot ID)
restic snapshots --path /my-app-backup.tar

# 2. Forget + prune in one step
restic forget <snapshot-id> --prune
```

If prune fails (OOM, lock), split into separate steps:

```bash
restic forget <snapshot-id>          # remove the snapshot reference
restic unlock --remove-all           # clear stale lock from crashed prune
restic prune                         # delete unreferenced data from S3
```

For large repos where prune OOMs in the operator pod, use Option B or C (see Restic Access).

---

## Retention / Pruning Old Backups

### Via Kubernetes

Use a Prune CR — applies retention rules and reclaims S3 storage:

```yaml
apiVersion: k8up.io/v1
kind: Prune
metadata:
  name: manual-prune
  namespace: my-app
spec:
  retention:
    keepLast: 5
    keepDaily: 14
    keepWeekly: 8
    keepMonthly: 6
```

⚠️ Retention rules are global to the repo. This will prune **all** backups (not just the namespace) based on these rules.

### Via Restic

```bash
restic forget --keep-last 5 --keep-daily 14 --prune
```

---

## Checking Repository Integrity

### Via Kubernetes

```yaml
apiVersion: k8up.io/v1
kind: Check
metadata:
  name: manual-check
  namespace: k8up-system
spec: {}
```

### Via Restic

```bash
restic check
```

---

## Unlocking a Stuck Repository

After a crashed or OOM-killed backup/prune job, the repo may remain locked.

```bash
# Remove own stale locks
restic unlock

# Force-remove all locks (only needed if unlock alone fails — e.g. lock held by a dead/restarted pod)
restic unlock --remove-all
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Prune exits 137 | OOM killed | Run as Job with higher memory limit |
| Repo locked after crash | Stale lock from dead pod | `restic unlock --remove-all` |
| Unwanted PVC backups | K8up backs up all PVCs by default | Add `k8up.io/backup: "false"` annotation to PVCs |
| Schedule exists but no backups | K8up uses internal scheduler, not CronJobs | Check operator logs, verify cron expression |
| "Nothing to backup" on manual Backup | No PVCs or PreBackupPods found | Ensure PreBackupPod CR exists in same namespace |

---

## Quick Reference

| Task | K8s | Restic |
|------|-----|--------|
| List backups | `kubectl get snapshots -n <ns>` | `restic snapshots --group-by path` |
| Trigger manual backup | Create Backup CR | — |
| Delete specific backup | — | `restic forget <id> --prune` |
| Retention cleanup | Prune CR | `restic forget --keep-last N --prune` |
| Check repo health | Check CR | `restic check` |
| Unlock stuck repo | — | `restic unlock --remove-all` |
| Exclude a PVC | `k8up.io/backup: "false"` annotation | — |