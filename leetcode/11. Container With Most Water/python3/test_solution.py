import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None


    def test_solution(self):
        height = [1,8,6,2,5,4,8,3,7]
        instance = solution.Solution() 
        result = instance.maxArea(height)

        print('\nResult: ', result)
        expected = 49
        self.assertEqual(expected, result)

suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


