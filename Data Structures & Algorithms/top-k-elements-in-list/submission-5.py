class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        result = []
        for a  in nums:
            if res.get(a, None) is None:
                res[a] = 1
            else:
                res[a] +=1
        result = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return result[:k]
        