import unittest     # Native test-package
import sut     # Tested script file


# Set up before first test-method of the module
def setUpModule():
    pass


# Test-class, name is free to choose
class KnownValues(unittest.TestCase):
    # Set up before first test-method of the class
    @classmethod
    def setUpClass(cls):
        pass

    # Set up before each test method
    def setUp(self):
        pass

    # Test-methods, name needs to begin with "test".
    def test_circle_area_for_radius_10(self):
        result = sut.circle_area(10)
        expected = 314.1592653589793
        self.assertEqual(expected, result)          # Actual test

    # Clean up after each test-method
    def tearDown(self):
        pass

    # Clean up after last test-method of the class
    @classmethod
    def tearDownClass(cls):
        pass


# Clean up after last test-method of the module
def tearDownModule():
    pass


# Run tests
if __name__ == '__main__':
    unittest.main()
