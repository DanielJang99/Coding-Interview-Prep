from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = {}
        for i, num in enumerate(nums):
            if (target-num) in records:
                return [i, records[target-num]]
            records[num] = i
        return []
        
