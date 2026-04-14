class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= [a for a in s]
        t = [a for a in t]
        if len(t)!=len(s):
            return False
        for a in s:
            if a in t:
                t.remove(a)
                # s.remove(a)
        
        if len(t) == 0:
            return True
        else:
            return False