import unittest
import solution

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        inputs = ["eat","tea","tan","ate","nat","bat"]
        # target = 0
        result = solution.Solution().groupAnagrams(inputs) 
        print('Result: ', result)
        expected = [["ate","eat","tea"],["bat"],["nat","tan"]]
        self.assertEqual(expected, result)





suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


