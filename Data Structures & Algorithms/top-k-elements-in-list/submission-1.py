class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for a in nums:
            if dic.get(a, None) is None:
                dic[a]= 0
            dic[a] = dic[a]+1
        nn = list(sorted(dic.values()))[-k:]
        res = []
        for a,v in dic.items():
            if v in nn:
                res.append(a)

        return res

        