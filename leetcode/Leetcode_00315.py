# 315. Count of Smaller Numbers After Self
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = []  # 有序数组

        def bisect_left(arr, x, low, high):
            left, right = low, high
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            # arr.insert(left, x)
            return left

        for i in range(n - 1, -1, -1):  # 反向遍历
            # pos = bisect.bisect_left(sl, nums[i])           # 找到右边比当前值小的元素个数
            pos = bisect_left(sl, nums[i], 0, len(sl))  # 找到右边比当前值小的元素个数
            res[i] = pos  # 记入答案
            sl.insert(pos, nums[i])  # 将当前值加入有序数组中

        return res
