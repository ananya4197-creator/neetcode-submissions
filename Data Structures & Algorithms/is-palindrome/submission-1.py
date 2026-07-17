class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''p =""
        for ch in s :
            if ch.isalnum():
               p += ch.lower()


        a = p[::-1]
        if a==p:
            return True

        return False'''
        p= ""
        for ch in s:
            if ch.isalnum():
                p += ch.lower()
        
        i = 0
        j = len(p)-1

        while i<=j:
            if p[i] != p[j]:
                return False
            else:
                i += 1
                j -= 1

        return True


