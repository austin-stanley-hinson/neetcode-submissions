class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //I have to use a set and then verify the sizes of the set and the original vector
        //prefer contains() for C++20 standard
        std::unordered_set<int> nums_set;

        for (int i : nums)
        {
            if (nums_set.contains(i))
            {
                return true;
            }
            nums_set.insert(i);
        }

        return false;
    }
};