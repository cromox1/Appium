__author__ = 'cromox'

from base.basehome import BaseHome
import utilities.custom_logger as cl
import logging
import os

class MotorsBase(BaseHome):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def motorsBaseParameters(self, installed=True):
        desired_caps_app = {}
        if installed is not True:
            desired_caps_app['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/motors.activities_2018-03-12.apk'))
        desired_caps_app['appPackage'] = 'com.motors.activities'
        desired_caps_app['appActivity'] = '.MainActivity'
        return desired_caps_app

    def gotoMotors(self):
        "Test the Motors app launches correctly, click Start button"
        self.continueButton("//*[@class='android.webkit.WebView' and @index='0']", "xpath")
        self.continueButton("//*[@class='android.view.View' and @index='5']", "xpath")
        # self.continueButton("start", "name")
        # self.continueButton("com.motors.activities:id/CrossProm_ExitButton")
        # sleep(2)

    def continueButton(self, locator, locatorType='id'):
        if self.isElementPresent(locator, locatorType) == True:
            self.elementClick(locator, locatorType)
