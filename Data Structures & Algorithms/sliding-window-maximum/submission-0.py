class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #nums arr must be of len >= k 
        if k > len(nums):
            return []

        win_map = {}
        res = []

        l = 0 
        for r in range(len(nums)):
            if nums[r] not in win_map:
                win_map[nums[r]] = 0
            win_map[nums[r]] += 1

            if (r - l + 1) == k:
                max_num = max(win_map.keys())
                res.append(max_num)
                win_map[nums[l]] -= 1 
                if win_map[nums[l]] == 0:
                    del win_map[nums[l]]
                l += 1 

        return res 

        '''
        nums = [1,2,1,0,4,2,6], k = 3

        win_map = {2:1, 6:1}
        res = [2,2,4, 4,6 ]

        [1,2,1,0,4,2,6]
                   l 
                        r



        '''
            
             


        
        
        
        '''
        {1: 1, 2:1, 0: 1}
        nums = [1,2,1,0,4,2,6]
                  l
                      r
        res = [2, ]
                r - l + 1 == k:
                    max(1,2,0)


        '''