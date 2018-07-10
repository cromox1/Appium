__author__ = 'cromox'

"""
@package base
ScreenDriver Factory class implementation
It creates a screendriver instance based on browser configurations
Example:
    sdf = ScreenDriverFactory(device)
    sdf.getScreenDriverInstance(apps)
"""
# import traceback
from appium import webdriver as webdriverappium

class ScreenDriverFactory():

    def __init__(self, device):
        """
        Inits ScreenDriverFactory class
        Returns:
            None
        """
        self.device = device

    def mobileDeviceParameter(self, device):
        self.desired_caps = {}
        if device == 'Nexus S API 23' or device == 'default' or device == 'test1':
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'roslitest_NexusS_API_23'
        elif device == 'Galaxy Nexus API 23' or device == 'galaxy' or device == 'test2':
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'roslitest2_Galaxy_Nexus_API_23'
        else:
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'roslitest_NexusS_API_23'
        print('\nDES_CAPS = ' + str(self.desired_caps) + '\n')
        return self.desired_caps

    def getScreenDriverInstance(self, mobileapp):
        """
        Get ScreenDriver Instance based on the mobile screen configuration
        Returns:
            'ScreenDriver Instance'
        """

        desired_caps = self.mobileDeviceParameter(self.device)
        if desired_caps == {} or mobileapp == {} or mobileapp is None:
            return
        else:
            desired_caps.update(mobileapp)
            self.driver = self.driverAppiumRemote(desired_caps)

            # Setting Driver Implicit Time out for An Element
            self.driver.implicitly_wait(3)

            return self.driver

    def driverAppiumRemote(self, desired_caps):
        appium_server_port = 'localhost:4723'
        return webdriverappium.Remote('http://' + appium_server_port + '/wd/hub', desired_caps)