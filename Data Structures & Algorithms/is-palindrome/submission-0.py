class Solution:
    def isPalindrome(self, s: str) -> bool:
        p =""
        for ch in s :
            if ch.isalnum():
               p += ch.lower()


        a = p[::-1]
        if a==p:
            return True

        return False