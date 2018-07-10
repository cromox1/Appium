__author__ = 'cromox'

"""
Example script to run one test against the Chess Free app using Appium

The test will:
- launch the app
- click the 'PLAY!' button
"""

# import os
import unittest
from appium import webdriver
# from time import sleep

class ChessAndroidTests(unittest.TestCase):
    def setUp(self):
        #desired_caps = {}
        #desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '6.0'
        #desired_caps['deviceName'] = 'roslitest_NexusS_API_23'

        desired_caps = {'platformName': 'Android', 'deviceName': 'roslitest_NexusS_API_23', 'platformVersion': '6.0'}

        # Returns abs path relative to this file and not cwd
        # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
        #desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        #desired_caps['appActivity'] = '.ChessFreeActivity'

        desired_app = {}
        # desired_caps_app['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
        desired_app['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_app['appActivity'] = '.ChessFreeActivity'

        desired_caps.update(desired_app)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('test = ' + str(self.driver.desired_capabilities))
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('\ndesired_capabilities = ' + str(self.driver.desired_capabilities) + '\n')

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):

        element1 = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/YesButton")
        # element1 = self.driver.find_element_by_name("Accept")
        if self.checkIsDisplayed(element1) == True:
            element1.click()

        element2 = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/ButtonPlay")
        # element2 = self.driver.find_element_by_name("ButtonPlay")
        if self.checkIsDisplayed(element2) == True:
            element2.click()

        element3 = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/CrossProm_ExitButton")
        if self.checkIsDisplayed(element3) == True:
            element3.click()

        # sleep(5)

    def checkIsDisplayed(self, element):
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")
        return element.is_displayed()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


