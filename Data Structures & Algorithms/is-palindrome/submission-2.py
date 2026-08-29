class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        -use two-pointer approach 
        -place one at either ends 
        -if not alphanumeric on either sides skip over
        -otherwise compare and check for mismatch 
        '''

        def isAlphaNumeric(char):
            return 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122
        

        #EdgeCase: an empty string
        if not s:
            return True 
        
        l, r = 0, len(s) - 1

        while l < r:
            if not isAlphaNumeric(s[l]):
                l += 1
                continue 
            
            if not isAlphaNumeric(s[r]):
                r -= 1 
                continue 
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1 

        return True

        '''
        l = 2
        r = 23

    Input: s = "Was it a car or a cat I saw?"
                  l
                                        r




        ''' 

            



