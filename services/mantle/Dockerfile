# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /backend

COPY ../../ .

RUN pip3 install -r ./services/mantle/requirements.txt