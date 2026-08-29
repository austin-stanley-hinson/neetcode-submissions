class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        res = nums[0]
        for num in counter:
            if counter[num] > 1:
                res = num 

        return res 