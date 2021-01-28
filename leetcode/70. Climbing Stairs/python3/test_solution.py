import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        inputs = 20
        result = solution.Solution().climbStairs(inputs)
        print('Result: ', result)
        expected = 10946
        self.assertEqual(expected, result)





suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


