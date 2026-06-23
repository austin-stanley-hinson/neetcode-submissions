class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_seen = {} #num : index

        for idx, num in enumerate(nums):
            diff = target - num 
            if diff in nums_seen:
                return [nums_seen[diff], idx]
            nums_seen[num] = idx 
        
        '''
        3, 4, 5, 6 ... target = 7 
        nums_seen = {3:0}
        [1, 4], diff = 3

        #space is O(n)
        #time is O(n)


        '''
