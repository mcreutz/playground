Pushing images to the internal image registry:
```bash
docker tag <your-image-name>:<tag> <host>:32000/<your-image-name>:<tag>
# or docker tag <image-id> <host>:32000/<your-image-name>:<tag>
docker push <host>:32000/<your-image-name>:<tag>
```