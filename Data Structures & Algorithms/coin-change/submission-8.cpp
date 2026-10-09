class Solution {
public:
    unordered_map<int,int> cache;
    int dfs(vector<int>& coins, int curr) {
        if (curr==0) return 0;
        if (cache.contains(curr)) return cache[curr];
        int best = 1e9;
        for (const auto& coin : coins) {
            if (curr-coin >=0) {
                best = min(best, 1+dfs(coins,curr-coin));
            }
        }
        cache[curr] = best;
        return best;
    }
    int coinChange(vector<int>& coins, int amount) {
        int res = dfs(coins, amount);
        return res < 1e9 ? res : -1;
    }
};
