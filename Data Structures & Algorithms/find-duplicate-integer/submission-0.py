class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_dict = Counter(nums)

        for k, v in count_dict.items():
            if v > 1:
                return k 
        
        return 