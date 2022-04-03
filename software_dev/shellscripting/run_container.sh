#! /bin/bash

# check if docker is installed, otherwise exit
if (! docker -v >/dev/null); then
    echo "Docker is not installed."
    exit 1
else
    echo "Docker is installed."
fi

# check if docker daemon is running, otherwise start it
if (! docker stats --no-stream &>/dev/null); then
    # On Mac OS this would be the terminal command to launch Docker
    echo -n "Docker daemon is not started. Starting Docker Deamon."
    open /Applications/Docker.app
    #Wait until Docker daemon is running and has completed initialisation
    while (! docker stats --no-stream &>/dev/null); do
        # Docker takes a few seconds to initialize
        echo -n "."
        sleep 1
    done
    echo ""
else
    echo "Docker daemon is running."
fi

# check if volume exists, otherwise create it
if (! docker volume list | grep postgres_barbucket >/dev/null); then
    echo "Volume does not exist. Creating volume."
    docker volume create postgres_barbucket >/dev/null
else
    echo "Volume exists."
fi

# check if container exists, otherwise create it
if (! docker container list -a | grep postgres_barbucket >/dev/null); then
    echo "Container does not exist. Creating container."
    docker container create \
    --name postgres_barbucket \
    -e POSTGRES_USER=barbucket \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_DB=barbucket \
    -p 5432:5432 \
    -v postgres_barbucket \
    postgres \
    >/dev/null
else
    echo "Container exists."
fi

# check if container is started, otherwise start it
if (! docker ps | grep postgres_barbucket >/dev/null); then
    echo "Container is not started. Starting container."
    docker container start postgres_barbucket >/dev/null
else
    echo "Container is started."
fi