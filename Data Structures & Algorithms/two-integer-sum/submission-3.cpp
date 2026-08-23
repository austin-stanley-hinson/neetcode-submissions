class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //task: find two nums that sum up to target and return their indices - smaller first
        //strat: use a hashmap and look up for complements. 
       //hashmap design: num -> index

       std::unordered_map<int, int> indexMap;

       for (int i = 0; i < nums.size(); ++i)
       {
        int curNum = nums[i];
        int complement = target - curNum;

        if (indexMap.contains(complement))
        {
            return {indexMap[complement], i};
        }

        indexMap[curNum] = i;
       } 
    return {};
    }
};
