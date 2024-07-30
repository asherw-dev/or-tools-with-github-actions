import unittest

# Example function to be tested
def add(a, b):
    return a + b

# Define the test case
class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-10, -5), -15)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-10, 5), -5)

# Run the tests
if __name__ == '__main__':
    unittest.main()
