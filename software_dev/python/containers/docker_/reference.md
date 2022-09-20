## Build an image from local dockerfile
`docker build -t <image-name>:<version> .`

## Run the image and show outputs
`docker run -it -p <host-port>:<image-port> <image-name>`
- Use `--entrypoint /bin/sh` or `.../bin/bash` to override entrypoint and start container shell instead
- Use `-d` insted of `-it` to launch container in background

## Execute command in runnning container
`docker exec -it <container-name> <command>`

## See all containers on host
`docker ps -a`

## Stop running container by name or id (shortening possible, id 123abc456... -> 123)
`docker stop <container-name>`
