# Helmfile CLI Cheatsheet

## Basic Commands

```bash
# Apply all releases from helmfile
helmfile sync          # Install or upgrade all releases. Will increment all relese versions and re-deploy resources with randomly generated content (e.g. Secrets)
helmfile apply         # Sync only if helmfile diff finds changes
# Delete all releases
helmfile destroy

# List releases
helmfile list

# Template releases locally
helmfile template

# Show changes before applying
helmfile diff          # Compare differences between current and desired state
helmfile diff --context 0  # Show minimal context in diff output
helmfile diff --concurrency 1  # No concurrent helm executions, would jumble output otherwise
```

## Common Flags

```bash
# Specify environment
helmfile --environment/-e staging,production sync

# Specify helmfile, defaulting to ./helmfile.yaml
helmfile --file/-f custom-helmfile.yaml sync

# Select specific releases from the helmfile
helmfile --selector/-l name=myapp sync
```

## Tips
- Use `helmfile deps` to update chart dependencies
- Use `helmfile status` to check release status
- Add `--debug` for verbose output
- Use `helmfile lint` to validate charts
- Use `diff` before `sync` to preview changes
- `apply` skips diff and interactive prompt, useful in CI/CD