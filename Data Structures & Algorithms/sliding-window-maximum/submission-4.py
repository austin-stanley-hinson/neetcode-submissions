class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #nums arr must be of len >= k 
        if k > len(nums):
            return []

        res = []
        max_idx = 0

        l = 0 
        r = 0
        while r < len(nums):
            if nums[r] > nums[max_idx]:
                max_idx = r

            if (r - l + 1) == k:
                res.append(nums[max_idx])
                if l == max_idx:
                    max_idx = l + 1
                    r = l 
                l += 1 
            
            r += 1

        return res 

        '''
        num = [1, -1]
        k = 1 
        res = [1,-1]
        max_idx = 0
        l = 1
        r = 1

        while r < 2:




        '''
            