FROM ubuntu:latest
MAINTAINER Vadim Markovtsev <vadim@sourced.tech>

COPY github_stars.py /
RUN apt-get update && apt-get install -y ca-certificates python3 python3-pip \
    && pip3 install --no-cache-dir PyGitHub \
    && apt-get remove -y python3-pip wget && apt-get -y autoremove && apt-get clean

ENV PYTHONIOENCODING utf-8
VOLUME /output
ENTRYPOINT ["python3", "-u", "/github_stars.py", "-i", "0f2000c351fb9b32a8b9ed2d2d2201df873885eb", "-o", "/output/repos.json"]
