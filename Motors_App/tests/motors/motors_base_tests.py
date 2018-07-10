__author__ = 'cromox'

from mobile.motors.motors_base import MotorsBase
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MotorsBaseTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        print('\n\nEVERY TESTS SETUP')

        desired_caps = self.driver.desired_capabilities
        mobileapp = {'appPackage': 'uk.co.aifactory.chessfree', 'appActivity': '.ChessFreeActivity'}
        desired_caps.update(mobileapp)
        from base.screendriverfactory import ScreenDriverFactory
        self.driver = ScreenDriverFactory.driverAppiumRemote(self.id(), desired_caps)
        self.tstatus = tStatus(self.driver)
        self.motorsbase = MotorsBase(self.driver)
        self.mobileapp = self.motorsbase.motorsBaseParameters()
        self.motorsbase.gotoMotors()

    @pytest.mark.run(order=1)
    def test_1goto_ChessFree(self):
        self.log.info("test_1goto_ChessFree started")
        print('TEST 1 = test_1goto_ChessFree')

    @pytest.mark.run(order=2)
    def test_2goto_ChessFree(self):
        self.log.info("test_2goto_ChessFree started")
        print('TEST 2 = test_2goto_ChessFree')

#driver = LoginPage
#ff = LoginTests()
