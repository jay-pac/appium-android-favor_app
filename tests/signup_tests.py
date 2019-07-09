from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def signup():
    desired_caps = {
        "platformName": "android",
        "deviceName": "Pixel 2 API 27",
        "appPackage": "com.neighbfav.neighborfavor",
        "appActivity": ".ui.entry.LaunchActivity",
        "udid": "emulator-5554",
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    TouchAction(driver).tap(None, 569, 1579, 1).perform()

    # Favor Signup
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_landing_get_started').click()
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_register_first_name').send_keys('Jason')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_register_last_name').send_keys('Pacitti')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_register_email').send_keys('jpacitti@gmail.com')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_register_phone').send_keys('512-750-8873')
    driver.find_element_by_id('com.neighbfav.neighborfavor:id/activity_register_password').send_keys('test_456')


signup()