FROM alpine:latest

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
            py3-pip \
            py3-setuptools \
            python3-dev

ARG workspace=/tmp/src
WORKDIR ${workspace}
# COPY . .