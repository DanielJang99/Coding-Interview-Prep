from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max=max(nums[i], current_max+nums[i])
            total_max=max(total_max, current_max)
        return total_max
        