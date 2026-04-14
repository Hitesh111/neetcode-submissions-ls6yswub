class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for a, num in enumerate(nums):
            search_int = target - num
            if search_int in seen:
                return [seen[search_int], a]
            seen[num] = a
        return []
