import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        m, n = 3, 7

        result = solution.Solution().uniquePaths(m, n) 
        print('Result: ', result)
        expected = 28
        self.assertEqual(expected, result)





suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


