docker build -t famba .

docker run -d --network host \
  -v "$(pwd)/data:/data" \
  --name famba famba