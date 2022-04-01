# 954. Array of Doubled Pairs

# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] =
# 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # dictionary to save count
        # sort arr to get from ...
        cnt = Counter(arr)
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True
