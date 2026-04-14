class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for a in strs:
            k = "".join(sorted(a))
            if k not in res:
                res[k] = []
            res[k].append(a)
        return  list(res.values())