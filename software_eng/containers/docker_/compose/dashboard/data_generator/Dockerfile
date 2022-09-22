FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y python3-dev
RUN apt upgrade -y python3-pip
RUN apt upgrade -y libpq-dev

WORKDIR /datagen

COPY . /datagen

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["data_generator.py"]