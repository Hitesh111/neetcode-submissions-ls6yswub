class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            num = nums[a]
            search_int = target - num
            for b in range(len(nums)):
                if a != b and search_int == nums[b]:
                    return [a,b]
