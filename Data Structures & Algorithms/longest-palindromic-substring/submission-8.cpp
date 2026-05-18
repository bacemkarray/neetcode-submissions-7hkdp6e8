class Solution {
public:
    string longestPalindrome(string s) {
        int res_length=0;
        string res_str="";

        for (int i=0; i<s.size(); i++) {
            int l = i;
            int r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r-l+1 > res_length) {
                    res_length = r-l+1;
                    res_str = s.substr(l,res_length);
                }
                l -= 1;
                r += 1;
            }

            l = i;
            r = i+1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r-l+1 > res_length) {
                    res_length = r-l+1;
                    res_str = s.substr(l,res_length);
                }
                l -= 1;
                r += 1;
            }
        }
        return res_str;
    }
};
