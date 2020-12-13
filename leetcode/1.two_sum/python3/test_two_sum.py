import unittest
import two_sum

class twoSumTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None


    def test_twoSum(self):
        nums = [2,7,11,15]
        target = 9
        sol = two_sum.Solution() 
        result = sol.twoSum(nums, target)
        print('result: ', result)


suite = (unittest.TestLoader()
                 .loadTestsFromTestCase(twoSumTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


