import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        inputs = [[1,3],[2,6],[8,10],[15,18]]
        # target = 0
        result = solution.Solution().merge(inputs) 
        print('Result: ', result)
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(expected, result)





suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


