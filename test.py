import unittest

from checker import Checker

class Tests(unittest.TestCase):

    def setUp(self):
        self.checker = Checker()

    def test_length_two(self):
        self.assertEqual(3, self.checker(2))

    def test_length_three(self):
        self.assertEqual(5, self.checker(3))

class TestPermutors(unittest.TestCase):
    result_2 = ['00', '01', '10', '11']
    result_3 = ['000', '001', '010', '011', '100', '101', '110', '111']

    def test_range_on_2(self):
        from checker import permute_by_range
        self.assertEqual(self.result_2, permute_by_range(2))

    def test_recursion_on_2(self):
        from checker import permute_by_recursion
        self.assertEqual(self.result_2, permute_by_recursion(2))

    def test_range_on_3(self):
        from checker import permute_by_range
        self.assertEqual(self.result_3, permute_by_range(3))

    def test_recursion_on_3(self):
        from checker import permute_by_recursion
        self.assertEqual(self.result_3, permute_by_recursion(3))

if __name__ == "__main__":
    unittest.main()

        

