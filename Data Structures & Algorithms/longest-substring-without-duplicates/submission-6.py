class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use a hashset to keep track of characters in a window, shrink until valid, record length
        update max_len if neccessary
        '''
        if not s:
            return 0

        max_len = 0
        char_set = set()

        l = 0 
        r = 0

        while r < len(s):

            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1 

            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


        '''
        "zxyzxyz"
           l 
              r

        char_set = {y, z, x}
        max_len = 3

        l = 2
        r = 5



        '''
