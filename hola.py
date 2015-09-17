# To install the Python client library:
# pip install -U selenium
import time

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# http://selenium-python.readthedocs.org/en/latest/api.html
caps = DesiredCapabilities.CHROME
myselenium = 'http://localhost:4444/wd/hub'

# http://selenium-python.readthedocs.org/en/latest/getting-started.html#using-selenium-with-remote-webdriver
driver = webdriver.Remote(command_executor=myselenium, desired_capabilities=caps)
time.sleep(0.5)

# Test: https://code.google.com/p/chromium/issues/detail?id=519952
pageurl = "http://www.google.com/adwords"
print "Opening page %s" % pageurl
driver.get(pageurl)
time.sleep(0.5)

print "Current title: %s" % driver.title
print "Asserting 'Google Adwords' in driver.title"
assert "Google AdWords" in driver.title

pageurl = "http://www.python.org"
print "Opening page %s" % pageurl
driver.get(pageurl)
time.sleep(0.5)

print "Asserting 'Python' in driver.title"
assert "Python" in driver.title

print "Finding element by name: q"
elem = driver.find_element_by_name("q")

print "Sending keys 'pycon'"
elem.send_keys("pycon")
time.sleep(0.5)

print "Sending RETURN key"
elem.send_keys(Keys.RETURN)

print "Ensure no results were found"
assert "No results found." not in driver.page_source

print "Close driver and clean up"
driver.close()
time.sleep(0.5)

print "All done. SUCCESS!"
driver.quit()
