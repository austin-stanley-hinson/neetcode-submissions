class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force approach: 
        '''
        scan over and over again and find the combinations that give "target"
        '''

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []


    '''
    DRY RUN OF CODE: 
    
    [4,5,6] and target = 10

    i = 0 
    j = 2

    (4 + 6)


    '''