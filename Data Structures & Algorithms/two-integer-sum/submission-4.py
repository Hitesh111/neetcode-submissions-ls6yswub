class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        for i in range(len(nums)):
            tt = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == tt:
                    return [i,j]
        
