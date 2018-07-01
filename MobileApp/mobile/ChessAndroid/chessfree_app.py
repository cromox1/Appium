__author__ = 'cromox'

from base.basehome import BaseHome
import utilities.custom_logger as cl
import logging
# import os
# from appium import webdriver as WDappium
from time import sleep

class ChessAndroid(BaseHome):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
        #desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        #desired_caps['appActivity'] = '.ChessFreeActivity'

        # driver = webdriverappium.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver()

    def gotoChessFree(self):
        "Test the Chess app launches correctly and click on Play button"
        self.continueButton("uk.co.aifactory.chessfree:id/YesButton")
        self.continueButton("uk.co.aifactory.chessfree:id/ButtonPlay")
        self.continueButton("uk.co.aifactory.chessfree:id/CrossProm_ExitButton")
        # sleep(2)

    def continueButton(self, locatorid):
        if self.isElementPresent(locatorid) == True:
            self.elementClick(locatorid)

