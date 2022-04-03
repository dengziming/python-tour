# 5219. Maximum Candies Allocated to K Children
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        while left < right:
            middle = (left+right)//2
            # 如果 比 目标大，可能会需要继续往前
            if letters[middle] > target:
                right = middle
            # 如果 小于等于目标，那一定不是目标，往后
            else:
                left = middle + 1
        # 如果二分到最后是 0，需要确认一波，0 是否
        if left == len(letters)-1 and letters[-1] <= target:
            return letters[0]

        return letters[left]
