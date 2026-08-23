class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //I have to use a set and then verify the sizes of the set and the original vector
        std::unordered_set<int> nums_set;

        for (int i = 0; i < nums.size(); ++i)
        {
            nums_set.insert(nums[i]);
        }

        return nums_set.size() != nums.size();
    }
};