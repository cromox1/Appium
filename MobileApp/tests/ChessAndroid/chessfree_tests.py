__author__ = 'cromox'

from mobile.ChessFree.chessfree_app import ChessFree
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ChessFreeTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        print('\n\nEVERY TESTS SETUP')

        desired_caps = self.driver.desired_capabilities
        mobileapp = {'appPackage': 'uk.co.aifactory.chessfree', 'appActivity': '.ChessFreeActivity'}
        # print('\nmobileapp 2 = ' + str(mobileapp) + '\n')
        desired_caps.update(mobileapp)
        from base.screendriverfactory import ScreenDriverFactory
        self.driver = ScreenDriverFactory.driverAppiumRemote(self.id(), desired_caps)
        # print('\nDRIVER 2 = ' + str(self.driver) + '\n')
        self.tstatus = tStatus(self.driver)
        self.chessfree = ChessFree(self.driver)
        self.mobileapp = self.chessfree.chessFreeParameters()
        self.chessfree.gotoChessFree()

    @pytest.mark.run(order=1)
    def test_1goto_ChessFree(self):
        self.log.info("test_1goto_ChessFree started")

        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/EasyButton")
        #self.tstatus.recordStatus(result, "Single Player button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/MediumButton")
        #self.tstatus.recordStatus(result, "Two Player button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/LoadButton")
        #self.tstatus.recordStatus(result, "Load Saved Game button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/SettingsButton")
        #self.tstatus.recordStatus(result, "Options button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/AchievementsButton")
        #self.tstatus.recordStatus(result, "Achievements button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/LeaderboardsButton")
        #self.tstatus.recordStatus(result, "Leaderboards button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/StatsButton")
        #self.tstatus.recordStatus(result, "Statistic button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/HelpButton")
        #self.tstatus.recordStatus(result, "Rules Of Chess button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/HardButton")
        #self.tstatus.recordStatus(result, "Hard button verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/IconSpot2")
        #self.tstatus.recordStatus(result, "Spot Icon verified")
        #result = self.chessfree.isElementPresent("uk.co.aifactory.chessfree:id/ImageView01")
        #self.tstatus.recordStatus(result, "Top images verified", True, "test_1goto_ChessFree was successful")
        print('TEST 1 = test_1goto_ChessFree')

    @pytest.mark.run(order=2)
    def test_2goto_ChessFree(self):
        self.log.info("test_2goto_ChessFree started")

        print('TEST 2 = test_2goto_ChessFree')

#driver = LoginPage
#ff = LoginTests()