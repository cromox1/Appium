__author__ = 'cromox'

from mobile.ChessAndroid.chessfree_app import ChessAndroid
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
        self.tstatus = tStatus(self.driver)
        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
        #desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        #desired_caps['appActivity'] = '.ChessFreeActivity'
        self.chessandroid = ChessAndroid(self.driver)

    @pytest.mark.run(order=1)
    def test_1goto_ChessFree(self):
        self.log.info("test_1goto_ChessFree started")
        self.chessandroid.gotoChessFree()
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/EasyButton")
        self.tstatus.recordStatus(result, "Single Player button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/MediumButton")
        self.tstatus.recordStatus(result, "Two Player button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/LoadButton")
        self.tstatus.recordStatus(result, "Load Saved Game button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/SettingsButton")
        self.tstatus.recordStatus(result, "Options button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/AchievementsButton")
        self.tstatus.recordStatus(result, "Achievements button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/LeaderboardsButton")
        self.tstatus.recordStatus(result, "Leaderboards button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/StatsButton")
        self.tstatus.recordStatus(result, "Statistic button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/HelpButton")
        self.tstatus.recordStatus(result, "Rules Of Chess button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/HardButton")
        self.tstatus.recordStatus(result, "Hard button verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/IconSpot2")
        self.tstatus.recordStatus(result, "Spot Icon verified")
        result = self.chessandroid.isElementPresent("uk.co.aifactory.chessfree:id/ImageView01")
        self.tstatus.recordStatus(result, "Top images verified", True, "test_1goto_ChessFree was successful")

#driver = LoginPage
#ff = LoginTests()