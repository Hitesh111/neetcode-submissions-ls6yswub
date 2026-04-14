class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]  # make a new list without nums[i]
            nn = 1
            for a in temp:
                nn *= a
            res.append(nn)
        return res
