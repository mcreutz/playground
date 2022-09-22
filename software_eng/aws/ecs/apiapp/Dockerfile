FROM alpine:latest

RUN apk upgrade
RUN apk add python3-dev py3-pip

WORKDIR /apiapp

COPY . /apiapp

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--reload"]
CMD ["main:app"]
