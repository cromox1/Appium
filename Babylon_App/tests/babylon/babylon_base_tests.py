__author__ = 'cromox'

from mobile.babylon.babylon_base import BabylonBase
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BabylonBaseTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        print('\n\nEVERY TESTS SETUP')

        desired_caps = self.driver.desired_capabilities
        #babylonapppkg = BabylonBase.babylonBaseParameters(self)['appPackage']
        #babylonappxtvt = BabylonBase.babylonBaseParameters(self)['appActivity']
        #mobileapp = {'appPackage': babylonapppkg, 'appActivity': babylonappxtvt}
        mobileapp = BabylonBase.babylonBaseParameters(self.id())
        print('\nmobileapp 2 = ' + str(mobileapp) + '\n')
        desired_caps.update(mobileapp)
        from base.screendriverfactory import ScreenDriverFactory
        self.driver = ScreenDriverFactory.driverAppiumRemote(self.id(), desired_caps)
        print('\nDRIVER 2 = ' + str(self.driver) + '\n')
        self.tstatus = tStatus(self.driver)
        self.babylon = BabylonBase(self.driver)
        self.babylonapp = self.babylon.babylonBaseParameters()
        self.babylon.gotoBabylon()

    @pytest.mark.run(order=1)
    def test_1goto_Babylon(self):
        self.log.info("test_1goto_ChessFree started")
        print('TEST 1 = test_1goto_ChessFree')

    @pytest.mark.run(order=2)
    def test_2goto_Babylon(self):
        self.log.info("test_2goto_ChessFree started")
        print('TEST 2 = test_2goto_ChessFree')

#driver = LoginPage
#ff = LoginTests()