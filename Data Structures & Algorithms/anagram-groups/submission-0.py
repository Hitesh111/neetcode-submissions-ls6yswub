class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ll = []
        for a in strs:
            k = ''.join(sorted(a))
            if k  not in dic:
                dic[k] = []
            dic[k].append(a)
        return list(dic.values())    
            

        
            
    
        