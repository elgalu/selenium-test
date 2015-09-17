# Hello world selenium test

## Requisistes

    python --version #=> Python 2.7.6
    sudo pip install -U selenium

## Clone

    git clone https://github.com/elgalu/selenium-test.git
    cd selenium-test

## Run

    python hola.py

Sample output

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
