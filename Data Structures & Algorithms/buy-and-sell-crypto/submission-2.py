class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = [0]
        for i in range(len(prices)-1):
            left = prices[i]
            right = prices[i+1:]
            if right:
                right = max(right)
            result.append(right-left)
        return max(result)

