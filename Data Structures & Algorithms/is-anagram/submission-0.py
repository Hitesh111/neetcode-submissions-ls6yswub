class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [a for a in s]
        t = [a for a in t]
        dict_str_map_s = {}
        dict_str_map_t = {}
        if len(s)!= len(t):
            return False
        if len(s) <1:
            return True
        for string in  s:
            if dict_str_map_s.get(string, None) is None:
                dict_str_map_s[string]= 1
            else:
                dict_str_map_s[string]= dict_str_map_s[string]+1
        for string in  t:
            if dict_str_map_t.get(string, None) is None:
                dict_str_map_t[string]= 1
            else:
                dict_str_map_t[string]= dict_str_map_t[string]+1
        print(dict_str_map_s , "---------------")
        print(dict_str_map_t, "============")
        
        for string in s:
            print(dict_str_map_s.get(string), "=====", dict_str_map_t.get(string))
            if dict_str_map_s.get(string) != dict_str_map_t.get(string):
                return False
        return True