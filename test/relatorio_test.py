import unittest
import xmlrunner

if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), exit=False)
