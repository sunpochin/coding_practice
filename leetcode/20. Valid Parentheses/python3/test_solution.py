import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        input = "()[]{}"
        result = solution.Solution().isValid(input) 
        print('input: ', input, 'Result: ', result)
        expected = True
        self.assertEqual(expected, result)

        input = "([)]{}"
        result = solution.Solution().isValid(input) 
        print('input: ', input, 'Result: ', result)
        expected = False
        self.assertEqual(expected, result)


suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


