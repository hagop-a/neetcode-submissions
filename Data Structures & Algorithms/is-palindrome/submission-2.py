class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl, pr = 0, len(s)-1

        while (pl < pr):
            while (pl < pr and not self.isAlphaNum(s[pl])):
                pl += 1
            while (pr > pl and not self.isAlphaNum(s[pr])):
                pr -= 1
            if (s[pl].lower() != s[pr].lower()):
                return False
            pl += 1
            pr -= 1
        return True


    
    def isAlphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))