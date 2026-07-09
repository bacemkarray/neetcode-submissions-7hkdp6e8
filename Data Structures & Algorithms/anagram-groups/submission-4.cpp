class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int,26>,vector<string>> groups;
        vector<vector<string>> res;
        for (const auto& str : strs) {
            array<int,26> key = {0};
            for (const auto& c : str ) {
                key[c-'a'] += 1;
            }
            groups[key].push_back(str);
        }
        for (const auto& [key,val] : groups) {
            res.push_back(val);
        }
           
        return res;
    }
};
