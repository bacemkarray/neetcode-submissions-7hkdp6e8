class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen;
        int longest=0;
        int l=0;
        for (int r=0; r<s.size(); r++) {
            while (seen[s[r]] > 0) {
                seen[s[l]]--;
                l++;
            }
            seen[s[r]]++;
            longest = max(longest,r-l+1);
        }
        return longest;
    }
};
