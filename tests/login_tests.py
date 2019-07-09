from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


def login():
    desired_caps = {
        "platformName": "android",
        "deviceName": "Pixel 2 API 27",
        "appPackage": "com.neighbfav.neighborfavor",
        "appActivity": ".ui.entry.LaunchActivity",
        "udid": "emulator-5554",
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)

    # Favor Login
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_landing_login').click()
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_login_username').send_keys('jpacitti@gmail.com')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_login_password').send_keys('B@lls1978')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_login_login').click()


login()