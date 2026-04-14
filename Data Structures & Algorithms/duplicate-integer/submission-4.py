class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for a in nums:
            if a in seen:
                return True
            seen.append(a)
            # print(a,"----", seen)
        return False
        