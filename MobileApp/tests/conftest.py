__author__ = 'cromox'

import pytest
import sys
from base.screendriverfactory import ScreenDriverFactory as mobilescreen

@pytest.yield_fixture()
def setUp():
    print("\n\n--- > RUNNING METHOD LEVEL SETUP < ---\n\n")
    yield
    print("\n\n--- > RUNNING METHOD LEVEL TEARDOWN < ---\n\n")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, device):
    print("\n\n== > RUNNING ONE TIME SETUP < ==\n\n")
    print('Python Version = ' + sys.version)

    sdf = mobilescreen(device)
    print('\nDEVICE = ' + str(device) + '\n')

    ##############
    #
    mobileapp = {'appPackage': 'com.android.browser', 'appActivity': '.BrowserActivity'}

    driver = sdf.getScreenDriverInstance(mobileapp)

    print('\nDRIVER = ' + str(driver) + '\n')
    if request.cls is not None:
        print('\n----- > request.cls is not None')
        request.cls.driver = driver
    ##############

    yield

    print("\n\n== > RUNNING ONE TIME TEARDOWN < ==\n\n")

def pytest_addoption(parser):
    parser.addoption("--device")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")