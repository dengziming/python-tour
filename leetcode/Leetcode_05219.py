# 5219. Maximum Candies Allocated to K Children
from typing import List


class Solution:
    def maximumCandies(self, a: List[int], k: int) -> int:
        L = 0
        R = max(a)
        while L < R:
            M = (L + R + 1) // 2
            s = 0
            for i in a:
                s += i // M
            if s >= k:
                L = M
            else:
                R = M-1
        return L
