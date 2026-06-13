class Solution {
public:
    unordered_set<int> visited;
    unordered_map<int,vector<int>> adj;

    bool dfs(int crs, vector<vector<int>>& prerequisites) {
        if (visited.find(crs) != visited.end()) return false;
        if (adj[crs].empty()) return true;
        visited.insert(crs);
        for (int pre : adj[crs]) {
            if (!(dfs(pre, prerequisites))) return false;
        }
        visited.erase(crs);
        adj[crs] = {};
        return true;  
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (const auto& pre : prerequisites) {
            int c = pre[0];
            int p = pre[1];
            adj[c].push_back(p);
        }

        for (int i=0; i<numCourses; i++) {
            if (!(dfs(i,prerequisites))) return false;
        }
        return true;
    }
};
