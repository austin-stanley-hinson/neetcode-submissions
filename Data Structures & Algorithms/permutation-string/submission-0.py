class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        abc - abc, bac, cba, cab
        same chars, same freq 

        perms of s1 in s2 

        hash-based ds like hashmap since we have chars, freq[chars]

        a - z (26 chars) 
        abc
        freq array of size 26: 

        s1_freq = [1,1,1,0,0,...]
        s2_freq = [0,0,..1, 0, c]

        Input: s1 = "abc", s2 = "lecabee"

        x = 0
        y = 0 
        lecabee
         x 
           y

        '''
        #EdgeCase: s1 is smaller than s2
        if len(s2) < len(s1):
            return False

        s1_freq = [0] * 26 
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
    
        s2_freq = [0] * 26

        l, r = 0, 0 

        while r < len(s2):

            s2_freq[ord(s2[r]) - ord('a')] += 1

            while l < r and (r - l + 1) > len(s1):
                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1 
            
            if len(s1) == (r - l + 1) and s1_freq == s2_freq:
                return True 
            
            r+= 1

        return False 

        '''
        s1 = abc , s2 = edbac 

        s1_freq = [1,1,1,0,0]

        s2_freq = [1,1,1,0,0]

        l = 0 
        r = 3 

        edbac
          l 
            r


        '''














