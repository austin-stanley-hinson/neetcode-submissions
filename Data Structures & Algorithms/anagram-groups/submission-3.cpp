class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //create char counts for all words and group words that have same ones together

        std::unordered_map<string, vector<string>> freqToAnagrams;

        for (const string& word : strs) 
        {
            array<int, 26> charFreq{};

            for (char c : word)
            {
                ++charFreq[c - 'a'];
            }

            string key;

            for (int freq : charFreq)
            {
                key += to_string(freq);
                key += "#";
            }

            freqToAnagrams[key].push_back(word);
            
        }

        //now to get them out and return a new 2D vector
        std::vector<vector<string>> res{};

        for (const auto& entry : freqToAnagrams)
        {
            res.push_back(entry.second);
        }

        return res;


    }
};
