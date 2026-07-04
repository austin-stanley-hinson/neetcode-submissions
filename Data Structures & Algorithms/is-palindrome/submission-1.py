class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Use two pointers. Loop from Left to Right on one. Loop from Right to Left on the second.
        Skip over non-alphanumeric characters. Stop when the pointers meet.
        '''

        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue 

            if s[left].lower() != s[right].lower():
                return False 
            
            left += 1
            right -= 1
        
        return True 
