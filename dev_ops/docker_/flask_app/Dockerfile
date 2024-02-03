# FROM alpine:latest

# RUN apk upgrade
# RUN apk add python3-dev py3-pip

# WORKDIR /app

# COPY . /app

# RUN pip3 install -r requirements.txt

# EXPOSE 5000

# ENTRYPOINT ["python3"]
# CMD ["my_flask_app.py"]


FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y python3
RUN apt upgrade -y python3-pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["my_flask_app.py"]