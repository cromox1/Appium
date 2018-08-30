__author__ = 'cromox'

from base.basehome import BaseHome
import utilities.custom_logger as cl
import logging
import os

class ChessFree(BaseHome):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def chessFreeParameters(self, installed=True):
        desired_caps_app = {}
        if installed is not True:
            # Returns abs path relative to this file and not cwd
            desired_caps_app['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
        desired_caps_app['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps_app['appActivity'] = '.ChessFreeActivity'
        return desired_caps_app

    def gotoChessFree(self):
        "Test the Chess app launches correctly, click Play button and go to Settings"
        self.continueButton("uk.co.aifactory.chessfree:id/YesButton")
        self.continueButton("uk.co.aifactory.chessfree:id/ButtonPlay")
        self.continueButton("uk.co.aifactory.chessfree:id/CrossProm_ExitButton")
        # sleep(2)

    def continueButton(self, locatorid):
        if self.isElementPresent(locatorid) == True:
            self.elementClick(locatorid)