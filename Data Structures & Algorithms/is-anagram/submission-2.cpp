class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size())
        {
            return false;
        }

        array<int, 26> s_char_count = {};
        array<int, 26> t_char_count = {};

        for (int i = 0; i < s.size(); ++i)
        {
            s_char_count[s[i] - 'a'] += 1;
            t_char_count[t[i] - 'a'] += 1;
        }

        return s_char_count == t_char_count;
        
    }
};
