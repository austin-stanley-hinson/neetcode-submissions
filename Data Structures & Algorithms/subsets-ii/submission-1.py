class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        if not nums:
            return res

        cur_combo = []

        def backtrack(index):
            res.append(cur_combo.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                cur_combo.append(nums[i])
                backtrack(i+1)
                cur_combo.pop()

        backtrack(0)

        return res