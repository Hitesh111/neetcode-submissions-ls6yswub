class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            check_seen = target-num
            if check_seen in seen:
                return [seen[check_seen], i]
            seen[num] = i
        return []
        
