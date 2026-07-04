class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute Force approach: 
        triple nested loop to find 3 numbers that sum to 0

        Efficient Solution:
        sort the arr
        select an anchor via looping
        Find other 2 with two - pointers.



        nums = [-4,-1,-1,0,1,2]
        anchor = -4 
        '''

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == 0:
                    res.append([nums[i], nums[left] , nums[right]])

                    left += 1 
                    right -= 1 

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 

                elif cur_sum < 0:
                    left += 1 
                else:
                    right -= 1 

        return res


        '''
        [-4,-1,-1,0,1,2]
                  i 
                    l 
                      r 
        res = [[-1, -1, 2], [-1, 0, 1]]
        i = 2
        left = 3
        right = 5

        cur_sum = 





        '''
                    
