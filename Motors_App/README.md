# Appium

## Motors

### Motors.co.uk – Making car buying, selling and owning easy details

Motors.co.uk is a car search portal that aims to make car buying, selling and owning easy by empowering and enlightening automotive buyers and sellers with smart, intuitive tools.

Motors Automation Framework consise these directories:

1) apps (to store MobileApp's .apk files)
2) base
3) configfiles
4) pages
5) tests
6) utilities
7) screenshots (create by code automatically if error/fault happens)

To run tests (example) :

#### py.test -s -v tests/motors/motors_base_tests.py --device default

(all tests in 'tests' directory -- to run one by one)

To run all tests as a test suite :

#### py.test tests/test_suite_Motors.py --device nexus6
#### py.test -v tests/test_suite_Motors.py --device nexus6

DEFAULT values (if didn't supply) :

'--device' = 'Android Nexus S API 23'
