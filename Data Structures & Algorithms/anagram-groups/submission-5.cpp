class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> groups;
        vector<vector<string>> res;
        for (const auto& str : strs) {
            vector<int> count(26,0);
            for (char c : str ) {
                count[c-'a']++;
            }
            string key = to_string(count[0]);
            for (int i=1; i<26; i++) {
                key += ',' + count[i];
            }
            groups[key].push_back(str);
        }
        for (const auto& [key,val] : groups) {
            res.push_back(val);
        }
        return res;
    }
};
