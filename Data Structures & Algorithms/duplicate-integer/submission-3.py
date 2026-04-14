class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aa = {}
        for a in nums:
            if aa.get(a, None) is None:
                aa[a] = 1
            else:
                return True
        return False
        