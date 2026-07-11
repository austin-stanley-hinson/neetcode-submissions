class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1 

        min_num = float('inf')

        while l <= r:
            mid = l + (r - l)//2

            if nums[l] <= nums[mid]:
                min_num = min(nums[l], min_num)
                l = mid + 1 
            else:
                min_num = min(nums[mid], min_num)
                r = mid - 1 

        return min_num 

         
        
        '''
        nums = [3,4,5,6,1,2]
                      l
                       m
                       r
        
        l = 3
        m = 4
        r = 5
        min_num = 1
        

        '''



