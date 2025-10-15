´´´sh
helm plugin install https://github.com/databus23/helm-diff

helmfile diff \
    --context 1 \  # Show 1 line of context
    --concurrency 1 \  # Allow 1 concurrent operations
    --selector name=loki  # Only show changes for release "loki"

```