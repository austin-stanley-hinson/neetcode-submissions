class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []
        
        for i, temp in enumerate(temperatures):
            if not temp_stack:
                temp_stack.append((i, temp))
                continue 
            
            while temp_stack and temp_stack[-1][1] < temp:
                res[temp_stack[-1][0]] = i - temp_stack[-1][0]
                temp_stack.pop()
            
            temp_stack.append((i, temp))

        return res 

        '''
        res = [ 1, 4 , 1 , 2 , 1, 0, 0]
        temp_stack = [(5,40), (6,28) ]

        [30,38,30,36,35,40,28]
        i = 6
        t = 28






        '''

