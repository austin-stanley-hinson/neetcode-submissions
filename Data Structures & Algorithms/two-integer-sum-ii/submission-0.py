class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach:
        # move l forward if cur_sum < target 
        # move r backwards if cur_sum > target
        #return l+1, r + 1

        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum < target:
                l += 1 
            elif cur_sum > target:
                r -= 1 
            else:
                break 

        return [l+1, r+1]

        #Dry Run 
        '''
        target = 3
        1 2 3 4.   l = 0, r = 1
        l.r 



        '''
