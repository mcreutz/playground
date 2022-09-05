FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y python3
RUN apt upgrade -y python3-pip

WORKDIR /datagen

COPY . /datagen

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["data_generator.py"]