class Solution {
public:

    string encode(vector<string>& strs) {
        //need to take an array of words, encode it into something predictable.
        // that would let me decode it.
        string res;
        for (string str : strs) {
            int length = str.size();
            res += to_string(length) + "*" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;

        int i=0;
        while (i < s.size()) {
            string len="";
            while (s[i] != '*') {
                len += s[i];
                i++;
            }
            res.push_back(s.substr(i+1,stoi(len)));
            i += 1+stoi(len);
        }
        return res;
    }
};
