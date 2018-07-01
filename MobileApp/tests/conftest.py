__author__ = 'cromox'

import pytest
import sys
from base.webdriverfactory import WebDriverFactory as mobiledesktop

@pytest.yield_fixture()
def setUp():
    print("\n--- > Running method level setUp")
    yield
    print("\n--- > Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, device):
    print("\n== > Running one time setUp")
    print('Python Version = ' + sys.version)

    wdf = mobiledesktop(device)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield

    print("\n== > Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--device")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
