FROM arm32v7/debian:buster

RUN apt update \
    && apt upgrade -y \
    && apt install nano -y \
    && apt clean

RUN mkdir /pics
ENTRYPOINT ["tail", "-f", "/dev/null"]
