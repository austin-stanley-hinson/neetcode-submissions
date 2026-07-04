class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Use a hashset to avoid duplicate work and find start of sequences
        '''

        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue 
            
            streak = 1 
            next_num = num + 1

            while next_num in nums_set:
                streak += 1 
                next_num += 1 

            longest_sequence = max(longest_sequence, streak)

        return longest_sequence 

        '''
        nums = [2,20,4,10,3,4,5]
        
        nums_set = [2,20,10,3,4,5]

        longest = 4

        cur = 10
        streak = 1
        next_num = 21
      



        '''
            
