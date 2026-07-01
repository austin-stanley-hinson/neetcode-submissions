class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False 
        
        t_lett_count = [0]*26 
        s_lett_count = [0]*26 

        for i in range(len(s)):
            t_lett_count[ord(t[i]) - ord('a')] += 1 
            s_lett_count[ord(s[i]) - ord('a')] += 1 


        return t_lett_count == s_lett_count