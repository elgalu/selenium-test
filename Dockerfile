FROM python:3.5.0

MAINTAINER Leo Gallucci <elgalu3@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

#========================
# Miscellaneous packages
#========================
RUN apt-get update -qqy \
  && apt-get -qqy install \
    unzip \
  && rm -rf /var/lib/apt/lists/*

# Check the README.md to see how to run this with docker-selenium
ENV SEL_HOST=localhost \
    SEL_PORT=24444

# What we need to run the tests
ADD . /root/selenium-test

RUN cd /root/selenium-test \
  && pip install --upgrade -r requirements.txt

ADD hola /usr/bin/

CMD hola
