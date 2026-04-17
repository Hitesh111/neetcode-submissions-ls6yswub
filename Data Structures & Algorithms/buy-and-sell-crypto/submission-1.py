class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = [0]
        for i in range(len(prices)-1):
            right = 0
            left = prices[i]
            right = prices[i+1:]
            if right:
                right = max(right)
            # print(left, right)
            result.append(right-left)
        # print(result)
        return max(result)

