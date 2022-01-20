from typing import List


def missingNumber(self, nums: List[int]) -> int:
    # for i in range(len(nums)+1):
    #     if i not in nums:
    #         return i
    
    # i = 0
    # while(True):
    #     if i not in nums:
    #         return i
    #     i +=1 
    
    n = len(nums)
    return ((n * (n+1)) // 2) - sum(nums) #same as sum(n+1) - sum(n)
