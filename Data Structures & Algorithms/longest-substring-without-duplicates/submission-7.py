class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hash-based data structure to detect duplicates
            -hashset()
        sliding window 
        shrinking strat: when I see a char already in the set()

        calculate its length (after shrinking/or not) update max_len if necc

        adding the char should be the last thing
        adding it to the seen set() after 

        Input: s = "zxyzxyz", output = 3
        max_len = 3
        seen = {y, z}
        l = 1 
        r = 4
        zxyzxyz
         l 
            r
        (r - l + 1) = 3

        {}
        axx
           l
           r

        '''

        #EdgeCase: when s is an emtpy string
        if not s:
            return 0

        max_len = 0 
        seen = set()

        l, r = 0, 0 

        while r < len(s):

            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1 

            max_len = max(max_len, r - l + 1)

            seen.add(s[r])
            r += 1 

        return max_len 














