#!/bin/bash

# check if in correct directory
if [ ! -f render.sh ] || [ ! -f deploy.sh ]; then
    echo "wrong directory"
    exit 1
fi

kapp deploy --diff-run --diff-changes --diff-context 12 -a ytt -f <(kustomize build platform_repo)  # --diff-changes-yaml
# "kapp deploy .. <(kustomize build ..)" is basically the same as "kustomize build .. | kapp deploy .. -f-" but kapp prefers it this way. See https://carvel.dev/kapp/docs/v0.45.0/faq/#error-asking-for-confirmation-eof#!/bin/bash
