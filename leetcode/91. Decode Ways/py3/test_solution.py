import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        inputs = [[1,1,1],[1,0,1],[1,1,1]]
        solution.Solution().setZeroes(inputs)
        print('inputs: ', inputs)
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertEqual(expected, inputs)





suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


