class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''ss = "".join(sorted(s))
        ts = "".join(sorted(t))

        if ss == ts:
            return True

        return False'''
        '''if len(s) != len(t):
            return False

        for i in s:
            flag = False
            for j in t:
                if i == j:
                    flag = True
            if not flag:
                return False
        return True'''

        if len(s) != len(t):
           return False


        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] =0
        
            seen[s[i]]+=1

        for j in range(len(t)):
            if t[j] not in seen:
                seen[t[j]]= 0
        
            seen[t[j]]-=1


        for key,value in seen.items():
            if value!= 0:
               return False

        return True



