class Solution:
    def isPalindrome(self, s: str) -> bool:
        s ="".join(a.lower() for a in s if a.isalnum())
        back = -1
        if len(s)%2 == 0:
            n= len(s)//2
        else:
            n = (len(s)//2)+1
        print(n)
        left = s[n:]
        right = s[:-n][::-1] 
        return left == right