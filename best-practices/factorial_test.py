# Example unittest of fucntion factorial

 

from factorial import factorial

import unittest

 

class TestFactoiral(unittest.TestCase):

    # test results for several values

    def test_factorial(self):

        self.assertAlmostEqual( factorial(3),6)

        self.assertAlmostEqual( factorial(1),1)

        self.assertAlmostEqual( factorial(0),1)

        self.assertAlmostEqual( factorial(5),120)

        # other assert methods: assertNotAlmostEqual, assertGreater, assertGreaterEqual, AssertLess, assertLessEqual, asserCountEqual, assertRegex

   

    # does it handle

    def test_input_value(self):

        self.assertRaises(TypeError, factorial, True)