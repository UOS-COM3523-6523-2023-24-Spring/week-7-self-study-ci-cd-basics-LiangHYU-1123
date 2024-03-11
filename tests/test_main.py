import unittest
from main import simple_count, complex_function


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    # def test_complex_function(self):
    #     self.assertEqual('behaviour 1', complex_function())
    # Simulation: Simulating a dependent function, such as a random function, in order to control its return value, allowing various cases to be tested deterministically.
    # Parameter injection: Enables deterministic testing by modifying the function to accept additional parameters to control the test behavior.
    # Statistical testing: Run the test multiple times and use statistical methods to verify that the resulting distribution is as expected.
    # Behavioral testing: Focusing on the impact or resulting state of a function rather than its direct output.
