import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        # Input: nums = [4,5,6,7,0,1,2], target = 0
        # Output: 4

        nums = [4,5,6,7,0,1,2]
        target = 0
        result = solution.Solution().search(nums, target) 
        print('Result: ', result)
        expected = 4
        self.assertEqual(expected, result)


        nums = [4,5,6,7,0,1,2]
        target = 3
        result = solution.Solution().search(nums, target) 
        print('Result: ', result)
        expected = -1
        self.assertEqual(expected, result)



suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


