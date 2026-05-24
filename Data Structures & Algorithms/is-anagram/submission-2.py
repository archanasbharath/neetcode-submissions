from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if sorted(s) == sorted(t):
            return True
        return False
        
        if Counter(s) == Counter(t):
            return True
        return False
        '''
        if len(s) != len(t):
            return False
        s_list = [0]*26
        t_list = [0]*26
        for i in range(len(s)):
            s_list[ord(s[i])-ord('a')] += 1
            t_list[ord(t[i])-ord('a')] += 1
        return s_list == t_list



        