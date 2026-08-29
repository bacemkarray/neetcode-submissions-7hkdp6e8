class Solution {
public:
    unordered_map<int,vector<int>> adj;
    unordered_set<int> visited;
    int res=0;

    bool dfs(int curr, vector<vector<int>>& edges) {
        if (visited.contains(curr)) return false;
        visited.insert(curr);

        for (int neighbor : adj[curr]) {
            if (visited.contains(neighbor)) continue;
            dfs(neighbor,edges);
        }
        return true;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        for (const auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        for (int i=0; i<n; i++) if (dfs(i,edges)) res++;
        return res;
    }
};
