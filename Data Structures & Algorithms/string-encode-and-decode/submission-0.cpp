class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedStr;

        for (const string& word : strs)
        {
            encodedStr += "#";
            encodedStr += to_string(word.size());
            encodedStr += "#";
            encodedStr += word;
        } //#5#Hello#5#World

        return encodedStr;
    }

    vector<string> decode(string s) {
        if (s.size() == 0)
        {
            return {};
        } //size == 11
        
        vector<string> res{};

        int i{0};
        int j{1};

        while (j < s.size())
        {
            if (s[j] == '#')
            {
                int curStrSize = stoi(s.substr(i + 1, (j - i - 1)));
                res.push_back(s.substr(j + 1, curStrSize));
                i = j + curStrSize + 1;
                j = i;
            }
            ++j;
        }

        return res;
    }
};
