# MobileApp

## APPIUM

Automation Framework directories:

1) base
2) configfiles
3) mobile
4) tests
5) utilities
6) apps (to store MobileApp's .apk files)
7) screenshots (create by code automatically if error/fault happens)

To run tests (example) :

* py.test -s -v tests/ChessAndroid/chessfree_tests.py --device default

(all tests in 'tests' directory -- to run one by one)

To run specific test from main test set :

* py.test.exe -v -s tests/ChessAndroid/chessfree_tests.py::LoginTests::test_FirewallSettingBlock
* py.test.exe -v -s tests/ChessAndroid/chessfree_tests.py::LoginTests::test_FirewallSettingOff

To run all tests as a test suite :

* py.test tests/test_suite_MobileApp_Appium.py   
* py.test -v tests/test_suite_MobileApp_Appium.py

DEFAULT values (if didn't supply) :

'--device' = 'Android Nexus S API 23'
