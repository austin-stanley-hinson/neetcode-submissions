class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 

        while left <= right: 
            mid = left + (right - left)//2 

            if nums[mid] == target:
                return mid 
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else: 
                    right = mid - 1 
            
        return -1 

        '''
        nums = [3,5,6,0,1,2], target = 4

        [3,5,6,0,1,2]
             l
           m
           r

        5 <= 4 < 5


        left = 2
        right = 1

        mid = 1 + (1 - 1)//2 = 1




        '''
