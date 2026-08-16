class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        

        '''

        res = []
        seen = set()

        if not nums:
            return res 
        
        res.append([])
        
        def backtrack(cur_index, combo):

            if cur_index >= len(nums):
                return 
            new_combo = combo[:]
            new_combo.append(nums[cur_index])

            if tuple(new_combo) not in seen:
                res.append(new_combo)
                seen.add(tuple(new_combo))
            else:
                return
            
            for i in range(cur_index + 1, len(nums)):
                backtrack(i, new_combo)

        for i in range(len(nums)):
            backtrack(i, [])

        return res 

        






