from ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Faster solution but with O(n) memory
#         s = set()
#         for n in nums:
#             if n in s:
#                 s.remove(n)
#             else:
#                 s.add(n)
        
#         return s.pop()

        # Slightly slower solution but with O(1) memory
        res = 0
        for num in nums:
            res ^= num
        return res