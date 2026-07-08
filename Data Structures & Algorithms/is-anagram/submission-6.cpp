class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> freq_s;
        unordered_map<char,int> freq_t;
        if (s.size() != t.size()) return false;
        // for (char i='a'; i < 'z'; i++) {
        //     freq_s[i] = 0;
        //     freq_t[i] = 0;
        // }
        for (int i=0; i<s.size(); i++) {
            freq_s[s[i]] = 1 + freq_s[s[i]];
            freq_t[t[i]] = 1 + freq_t[t[i]]; 
        }
        
        for (char i='a'; i < 'z'; i++) if (freq_s[i] != freq_t[i]) return false;
        return true;
    }
};
