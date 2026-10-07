class Solution {
public:
    unordered_map<string,int> cache;
    int dfs(string s, int i) {
        if (cache.contains(s.substr(0,i))) return cache[s.substr(0,i)];
        if (i == s.size()) return 1;
        if (s[i]=='0') return 0;
        int res = dfs(s,i+1);
        if (i+1<s.size() && (s[i]=='1' || (s[i]=='2' && s[i+1]<'7'))) {
            res += dfs(s,i+2);
        }
        cache[s.substr(0,i)] = res;
        return res;
    }

    int numDecodings(string s) {
        return dfs(s,0);
    }
};
