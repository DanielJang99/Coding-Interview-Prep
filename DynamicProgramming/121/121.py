from ast import List


def maxProfit(prices: List[int]) -> int:
    left, right, ans = 0, 1, 0
    if prices:
        while(right < len(prices)):
            if prices[left] < prices[right]:
                ans = max(ans, prices[right]-prices[left])
            else:
                left = right
            right +=1 
    return ans

