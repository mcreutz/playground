# check if in correct directory
if [ ! -f render.sh ] || [ ! -f deploy.sh ]; then
    echo "wrong directory"
    exit 1
fi

# delete rendered patches from 'patches_rendered' directory
rm platform_repo/patches_rendered/*

# render the patch templates
ytt \
    -f platform_repo/patch_templates \
    -f platform_repo/default_values.yaml \
    --data-values-file cluster_repo/values.yaml \
    --output-files platform_repo/patches_rendered