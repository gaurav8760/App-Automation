import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver


# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps = [

    {
        "deviceName": "Galaxy S9",
        "platformName": "android",
        "platformVersion": "10",
        "app": "lt://APP1001131637005466834502",
        "build": "Android 3",
        "isRealMobile": True,
        "newCommandTimeout": 60,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "build": "Demo Test Run : App Automation Galaxy S9 --1",
         # "infraTimeout": 100,
        # "devicelog": True,
        # "tunnel": True,
        #  "geoLocation": "BR",
        # "appPackage": "org.wikipedia",
        # "tunnel": True,
        # "appActivity": ".main.MainActivity",
    },
    {
        "deviceName": "Galaxy S9",
        "platformName": "android",
        "platformVersion": "10",
        "app": "lt://APP1001131637005466834502",
        "isRealMobile": True,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "build": "Demo Test Run : App Automation Galaxy S9 --2",
        # "devicelog": True,
        # "tunnel": True,
        # "tunnel": True,
        # "infraTimeout": 100,
        #  "geoLocation": "BR",
        # "appPackage": "org.wikipedia",
        # "appActivity": ".main.MainActivity",
    },
    {
        "deviceName": "Galaxy S9",
        "platformName": "android",
        "platformVersion": "10",
        "app": "lt://APP1001131637005466834502",
        "isRealMobile": True,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "build": "Demo Test Run : App Automation Galaxy S9 --3",
        # "appPackage": "org.wikipedia",
        # "infraTimeout": 100,
        # "tunnel": True,
        # "appActivity": ".main.MainActivity",
        # "devicelog": True,
        # "tunnel": True,
        #  "geoLocation": "BR",
    },
    {
        "deviceName": "Galaxy S9",
        "platformName": "android",
        "platformVersion": "10",
        "app": "lt://APP1001131637005466834502",
        "isRealMobile": True,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "build": "Jovive Robot-Automation Test - 22",
        "deviceOrientation": "PORTRAIT",
        "performance": False,
        "network": False,
        "visual": False,
        "console": True,
        "w3c": False,
        "tunnel": False,
        "tunnelIdentifier":"",
        "version": "",
        "video": True,
        "userAgent":"selenium/3.141.0 (python windows)"
        # "infraTimeout": 100,
        # "devicelog": True,
        # "appPackage": "org.wikipedia",
        # "infraTimeout": 100,
        # "tunnel": True,
        # "appActivity": ".main.MainActivity",
        # "devicelog": True,
        # "tunnel": True,
        #  "geoLocation": "BR",
    },

]
# run_session function searches for 'lambtest' on google.com


def run_session(desired_cap):
    driver = webdriver.Remote(
        # hub.mobile-dev-1.dev.lambdatest.io/wd/hub",
        command_executor="https://gauravkb:DqLVVOF1ll4TTMyXXt3gslp8NZ8Ynon3vwcRd4eFTV5GLavGh9@beta-hub.lambdatest.com/wd/hub",
        desired_capabilities=desired_cap)

    driver.get("https://bigfork.dev.aloe-2.com/account/login")
    time.sleep(5)
    # Test case for the lambdatest sample Android app.
    # If you have uploaded your app, update the test case here.

    print("Searching lambdatest on google.com ")
    time.sleep(2)
    username = driver.find_element_by_xpath("/html/body/app-root/app-auth/div/div[1]/div/div/app-login/form/aloe-input-text/aloe-form-control/div/nz-form-item/nz-form-control/div/div/nz-input-group/input")
    username.send_keys("aloe2admin")
    username.submit()

    time.sleep(2)
    password = driver.find_element_by_xpath("/html/body/app-root/app-auth/div/div[1]/div/div/app-login/form/fieldset/aloe-input-password/aloe-form-control/div/nz-form-item/nz-form-control/div/div/nz-input-group/input")
    password.send_keys("P@ssw0rD")
    password.submit()

    time.sleep(4)
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (MobileBy.XPATH, "/html/body/app-root/app-auth/div/div[1]/div/div/app-login/form/aloe-button/button"))
    )
    search_input.click()


# Invoke driver.quit() after the test is done to indicate that the test is completed.
    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel