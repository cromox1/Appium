__author__ = 'cromox'

import os
import unittest
from appium import webdriver
# from time import sleep

class ChessAndroidTests(unittest.TestCase):
    # "Class to run tests against the Chess Free app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'roslitest_NexusS_API_23'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/motors.activities_2018-03-12.apk'))
        apppackage = 'com.motors.activities'
        appxtvt = '.MainActivity'
        desired_caps['appPackage'] = apppackage
        desired_caps['appActivity'] = appxtvt
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # "Tear down the test"
        self.driver.quit()

    def test_single_player_mode(self):

        ## "Test the Chess app launches correctly and click on Play button"
        element1 = self.driver.find_element_by_id("com.motors.activities:id/YesButton")
        # element1 = self.driver.find_element_by_name("Accept")
        if self.checkIsDisplayed(element1) == True:
            element1.click()

        element2 = self.driver.find_element_by_id("com.motors.activities:id/ButtonPlay")
        # element2 = self.driver.find_element_by_name("ButtonPlay")
        if self.checkIsDisplayed(element2) == True:
            element2.click()
        # sleep(5)

    def checkIsDisplayed(self, element):
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")
        return element.is_displayed()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
