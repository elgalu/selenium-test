# selenium-test [![Build Status](https://travis-ci.org/elgalu/selenium-test.svg?branch=master)](https://travis-ci.org/elgalu/selenium-test)

Hello world selenium test.

If you want to see this running inside a docker container visit [selenium-test-dockerized][]

## Clone

    git clone https://github.com/elgalu/selenium-test.git
    cd selenium-test

## Requisistes
Add `sudo` only if you get permission denied.

    pip install --upgrade -r requirements.txt

It needs a selenium server, for example [docker-selenium][]

    docker run -d --name=myselenium elgalu/selenium:latest
    docker exec myselenium wait_all_done 30s
    export SEL_HOST=$(docker inspect -f='{{.NetworkSettings.IPAddress}}' myselenium)
    export SEL_PORT=24444

## Run

    python hola.py

Sample output

    Will connect to selenium at http://172.17.0.6:24444/wd/hub
    Opening page http://www.google.com/adwords
    Current title: Google AdWords | Pay-per-Click-Onlinewerbung auf Google (PPC)
    Asserting 'Google Adwords' in driver.title
    Opening page http://www.python.org
    Asserting 'Python' in driver.title
    Finding element by name: q
    Sending keys 'pycon'
    Sending RETURN key
    Ensure no results were found
    Close driver and clean up
    All done. SUCCESS!

## Sauce Labs
Works in Sauce Labs via http basic auth:

    export SAUCE_USER="your-sauce-labs-user"
    export SAUCE_KEY="****your-secret****"
    export SEL_HOST="${SAUCE_USER}:${SAUCE_KEY}@ondemand.saucelabs.com"
    export SEL_PORT=80
    python hola.py

## With docker
### Build

    docker build -t="elgalu/selenium-test" .

### Run

    export SEL_HOST=$(docker inspect -f='{{.NetworkSettings.IPAddress}}' myselenium)
    docker run --rm --name=test1 -ti -e SEL_HOST elgalu/selenium-test


[selenium-test-dockerized]: https://github.com/elgalu/selenium-test-dockerized
[docker-selenium]: https://github.com/elgalu/docker-selenium
