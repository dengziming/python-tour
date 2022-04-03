# 5219. Maximum Candies Allocated to K Children
import unittest
from typing import List

from leetcode.Leetcode_00744 import Solution


class TestSolution(unittest.TestCase):

    def test_canReorderDoubled(self):
        solution = Solution()
        self.assertEqual('c', solution.nextGreatestLetter(['c', 'f', 'j'], 'a'))
        self.assertEqual('f', solution.nextGreatestLetter(['c', 'f', 'j'], 'c'))
        self.assertEqual('f', solution.nextGreatestLetter(['c', 'f', 'j'], 'd'))

