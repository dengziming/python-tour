import unittest

from .Leetcode_00954 import Solution


class TestSolution(unittest.TestCase):

    def test_canReorderDoubled(self):
        solution = Solution()
        self.assertFalse(solution.canReorderDoubled([3, 1, 3, 6]))
        self.assertFalse(solution.canReorderDoubled([2, 1, 2, 6]))
        self.assertTrue(solution.canReorderDoubled([4, -2, 2, -4]))
