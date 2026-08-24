class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //couting sort/ bucket sort algorithm
        //have 2D vector, freq, where freq[i] holds all num that have freq i

        //build an unordered map where num : freq

        std::unordered_map<int, int> numToFreq{};

        //builds a counter hashtable 
        for (int num : nums)
        {
            ++numToFreq[num];
        }

        vector<vector<int>> freqBuckets(nums.size() + 1);

        //fill the frequency buckets
        for (const auto& [key, value] : numToFreq)
        {
            freqBuckets[value].push_back(key);
        }

        vector<int> res{};

        for (int i = freqBuckets.size() - 1; i > 0; --i){
            vector<int>& bucket = freqBuckets[i];
            for (int j = 0; j < bucket.size(); ++j)
            {
                if (res.size() < k)
                {
                    res.push_back(bucket[j]);

                }
                
                if (res.size() == k)
                {
                    return res;
                }
            }
        }

        return {};



    }
};
