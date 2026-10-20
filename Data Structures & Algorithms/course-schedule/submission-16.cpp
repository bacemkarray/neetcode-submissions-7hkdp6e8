class Solution {
public:
    unordered_map<int,vector<int>> adj;
    unordered_set<int> visited;

    bool dfs(int curr, vector<vector<int>>& prerequisites) {
        if (adj[curr].empty()) return true;
        if (visited.contains(curr)) return false;
        visited.insert(curr);

        for (const auto& course : adj[curr]) {
            if (!dfs(course, prerequisites)) return false;
        }
        visited.erase(curr);
        adj[curr] = {};
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (vector<int> pre : prerequisites) {
            adj[pre[0]].push_back(pre[1]);
        }
        
        for (int i=0; i<numCourses; i++) {
            if (!dfs(i,prerequisites)) return false;
        }
        return true;
    }
};
