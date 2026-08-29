class Solution {
public:
    unordered_map<int,vector<int>> adj;
    unordered_set<int> visited;
    int res;

    bool dfs(int parent, int curr, vector<vector<int>>& edges) {
        if (visited.contains(curr)) return false;
        visited.insert(curr);

        for (int node : adj[curr]) {
            if (node == parent) continue;
            dfs(curr,node,edges);
        }
        return true;
    }

    int countComponents(int n, vector<vector<int>>& edges) {
        res = 0;
        for (vector<int> edge : edges) {
            int a = edge[0];
            int b = edge[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        for (int i=0; i<n; i++) {
            if (dfs(-1,i,edges)) res++;
        }

        return res;
    }
};
