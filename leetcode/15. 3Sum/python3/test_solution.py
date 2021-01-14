import unittest
import solution
import ListNode

class solutionTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_solution(self):
        head = [1,2,3,4,5]
        n = 2
        instance = solution.Solution() 
        result = instance.removeNthFromEnd(head, n)

        print('\nResult: ', result)
        expected = 49
        self.assertEqual(expected, result)

suite = (unittest.TestLoader()
    .loadTestsFromTestCase(solutionTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)


