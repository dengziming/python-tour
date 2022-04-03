# 5219. Maximum Candies Allocated to K Children
import unittest
from typing import List

from leetcode.Leetcode_05219 import Solution


class TestSolution(unittest.TestCase):

    def test_canReorderDoubled(self):
        solution = Solution()
        self.assertEqual(3, solution.maximumCandies([1,2,3,4,10], 5))
