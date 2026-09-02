class Solution {
public:
    unordered_set<int> visited;
    unordered_map<int,vector<int>> adj;
    bool dfs(int parent, int curr) {
        if (visited.contains(curr)) return false; 
        visited.insert(curr);

        for (int neighbor : adj[curr]) {
            if (neighbor == parent) continue;
            if (!dfs(curr, neighbor)) return false;
        }
        return true;

    }
    bool validTree(int n, vector<vector<int>>& edges) {
        for (vector<int> edge : edges) {
            int a = edge[0];
            int b = edge[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        if (!dfs(-1,0)) return false;

        return visited.size() == n;

    }
};
