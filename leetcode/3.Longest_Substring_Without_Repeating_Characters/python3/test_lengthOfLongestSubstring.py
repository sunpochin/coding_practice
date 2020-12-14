import unittest
import lengthOfLongestSubstring

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None


    def test_lengthOfLongestSubstring(self):
        input = 'abcabcbb'
        solution = lengthOfLongestSubstring.Solution() 
        result = solution.lengthOfLongestSubstring('abcabcbb')
        print('\nResult: ', result)
        expected = 3
        self.assertEqual(expected, result)
        



suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


