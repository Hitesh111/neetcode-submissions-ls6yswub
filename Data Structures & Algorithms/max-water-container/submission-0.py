class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right  = 0, len(heights)
        result = []
        for left in range(len(heights)):
            for right in range(len(heights)):
                subb_len = len(heights[left: -right])
                subb = min(heights[left],heights[-right])
                res = subb* subb_len
                # print(res)
                result.append(res)
                
        return max(result)

                