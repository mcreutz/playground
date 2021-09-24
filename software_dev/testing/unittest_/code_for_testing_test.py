import unittest     # Native test-package
import code_for_testing     # Tested script file


# Test-class, name is free to choose
class KnownValues(unittest.TestCase):

    # Prepare for test-methods, create objects for example..
    def setUp(self):
        pass

    # Test-methods, name needs to begin with "test".
    def test_circle_area_for_radius_10(self):
        result = code_for_testing.circle_area(10)
        expected = 314.1592653589793
        self.assertEqual(expected, result)          # Actual test

    # Clean up after test-methods, garbage collection for example..
    def tearDown(self):
        pass
    

# Run tests
if __name__ == '__main__':
    unittest.main()