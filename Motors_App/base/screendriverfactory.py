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
        if device == 'test1' or device == 'Nexus S API 23' or device == 'default' or device is None:
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'roslitest_NexusS_API_23'
        elif device == 'test2' or device == 'Galaxy Nexus API 23' or device == 'galaxy':
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '6.0'
            self.desired_caps['deviceName'] = 'roslitest2_Galaxy_Nexus_API_23'
        elif device == 'test3' or device == 'Nexus 6 API 27' or device == 'nexus6':
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['platformVersion'] = '8.1'
            self.desired_caps['deviceName'] = 'rosli3_Nexus_6_API_27'
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
