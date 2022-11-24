#FROM python:3.8-slim-buster
FROM python:3.10-slim-bullseye
RUN python3 -m pip install --upgrade pip

COPY . ./project


WORKDIR /project

RUN pip3 install -r requirements.txt
RUN apt update && apt install make
WORKDIR /project/homework2
CMD ["make", "rest"]
