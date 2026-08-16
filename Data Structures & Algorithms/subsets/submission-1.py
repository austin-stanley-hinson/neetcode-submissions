class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        

        '''

        res = []
        if not nums:
            return res 
                        
        def backtrack(cur_index, cur_combo):
            res.append(cur_combo.copy())

            for i in range(cur_index, len(nums)):
                cur_combo.append(nums[i])
                backtrack(i + 1, cur_combo)
                cur_combo.pop()

            return 
        
        backtrack(0, [])


        return res 

        






