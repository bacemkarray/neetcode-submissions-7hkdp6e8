class Solution {
public:
    unordered_map<int,int> cache;
    int dfs(string s, int i) {
        if (cache.contains(i)) return cache[i];
        if (i == s.size()) return 1;
        if (s[i]=='0') return 0;
        int res = dfs(s,i+1);
        if (i+1<s.size() && (s[i]=='1' || (s[i]=='2' && s[i+1]<'7'))) {
            res += dfs(s,i+2);
        }
        cache[i] = res;
        return res;
    }

    int numDecodings(string s) {
        return dfs(s,0);
    }
};
