__author__ = 'cromox'

from base.basehome import BaseHome
import utilities.custom_logger as cl
import logging
import os

class BabylonBase(BaseHome):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def babylonBaseParameters(self, installed=True):
        self.babylonAppPackage = 'com.babylon'
        self.babylonAppActivity = '.PublicLauncherActivity'
        desired_caps_app = {}
        if installed is not True:
            desired_caps_app['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/Babylon_v3.23.0.11375.apk'))
        desired_caps_app['appPackage'] = self.babylonAppPackage
        desired_caps_app['appActivity'] = self.babylonAppActivity
        return desired_caps_app

    def gotoBabylon(self):
        "Test the Motors app launches correctly, click Start button"
        self.continueButton("//*[@class='android.webkit.WebView' and @index='0']", "xpath")
        self.continueButton("//*[@class='android.view.View' and @index='5']", "xpath")
        # self.continueButton("start", "name")
        # self.continueButton("com.motors.activities:id/CrossProm_ExitButton")
        # sleep(2)

    def continueButton(self, locator, locatorType='id'):
        if self.isElementPresent(locator, locatorType) == True:
            self.elementClick(locator, locatorType)
