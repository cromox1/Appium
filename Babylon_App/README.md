# Appium

## Babylon Health

### https://www.babylonhealth.com/ - Online Doctor Consultations & Advice 

Babylon is a personalised healthcare service that gives you access to appointments with qualified GPs for medical advice, either through a subscription or the NHS. It’s the convenient way to access GP appointments and obtain any necessary prescriptions, medical information (via our AI-powered symptom checker), from your phone.

Babylon's Automation Framework consise these directories:

1) apps (to store MobileApp's .apk files)
2) base
3) configfiles
4) pages
5) tests
6) utilities
7) screenshots (create by code automatically if error/fault happens)

To run tests (example) :

#### py.test -s -v tests/babylon/babylon_base_tests.py --device default

(all tests in 'tests' directory -- to run one by one)

To run all tests as a test suite :

#### py.test tests/test_suite_Babylon.py --device nexus6
#### py.test -v tests/test_suite_Babylon.py --device nexus6

DEFAULT values (if didn't supply) :

'--device' = 'Android Nexus S API 23'
