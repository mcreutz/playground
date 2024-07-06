#!/bin/bash

# check if in correct directory
if [ ! -f render.sh ] || [ ! -f deploy.sh ]; then
    echo "wrong directory"
    exit 1
fi

kapp deploy -a ytt -f <(kustomize build platform_repo)
# "kapp deploy .. <(kustomize build ..)" is basically the same as "kustomize build .. | kapp deploy .. -f-" but kapp prefers it this way. See https://carvel.dev/kapp/docs/v0.45.0/faq/#error-asking-for-confirmation-eof#!/bin/bash
