class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {")":"(", "}":"{", "]":"["}

        bracket_stack = []

        for br in s:
            if br not in bracket_map:
                bracket_stack.append(br)
                continue 

            if not bracket_stack:
                return False 

            if bracket_stack[-1] != bracket_map[br]:
                return False 
            else:
                bracket_stack.pop()
    
        return not bracket_stack

        '''
        ([{}])

        cur = )

        stack = 



        '''

            
            

            

