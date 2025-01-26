# Helmfile CLI Cheatsheet

## Basic Commands

```bash
# Apply all releases from helmfile
helmfile sync          # Install or upgrade all releases
helmfile apply         # Like sync but with no confirmation, use with caution

# Delete all releases
helmfile destroy

# List releases
helmfile list

# Template releases locally
helmfile template

# Show changes before applying
helmfile diff          # Compare differences between current and desired state
```

## Common Flags

```bash
# Specify environment
helmfile -e production sync

# Specify helmfile
helmfile -f custom-helmfile.yaml sync

# Select specific releases from the helmfile
helmfile --selector name=myapp sync

# Show diff before applying
helmfile diff
```

## Environment Management

```bash
# Apply with specific values file
helmfile -e staging sync

# Apply with multiple environments
helmfile -e staging,production sync
```

## Tips
- Use `helmfile deps` to update chart dependencies
- Use `helmfile status` to check release status
- Add `--debug` for verbose output
- Use `helmfile lint` to validate charts
- Use `diff` before `sync` to preview changes
- `apply` skips diff and interactive prompt, useful in CI/CD