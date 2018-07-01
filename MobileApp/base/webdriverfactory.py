__author__ = 'cromox'

"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
# import traceback
from appium import webdriver as webdriverappium
import os

class WebDriverFactory():

    def __init__(self, device):
        """
        Inits WebDriverFactory class
        Returns:
            None
        """
        self.device = device

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'roslitest_NexusS_API_23'

        if self.device == 'new':
            # Returns abs path relative to this file and not cwd
            desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/ChessFree.apk'))
            desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
            desired_caps['appActivity'] = '.ChessFreeActivity'
        else:
            desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
            desired_caps['appActivity'] = '.ChessFreeActivity'

        driver = webdriverappium.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('test1 = ' + str(driver.desired_capabilities))

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)

        # print('Appium Driver name ( ' + str(driver.name) + ' ) ' ) # + driver.capabilities[strver])

        return driver
