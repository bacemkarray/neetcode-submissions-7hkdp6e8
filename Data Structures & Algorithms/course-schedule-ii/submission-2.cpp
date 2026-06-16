class Solution {
public:
    vector<int> res = {};
    unordered_map<int,vector<int>> adj;
    unordered_set<int> visiting;
    unordered_set<int> visited;

    bool dfs(vector<vector<int>>& prerequisites, int crs) {
        if (visiting.find(crs) != visiting.end()) return false;
        if (visited.find(crs) != visited.end()) return true;

        visiting.insert(crs);
        if (!adj[crs].empty()) {
            for (const auto& pre : adj[crs]) {
                if (!dfs(prerequisites, pre)) return false;
            }
        }
        visiting.erase(crs);
        visited.insert(crs);
        res.push_back(crs);
        return true;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (const auto& pre : prerequisites) {
            adj[pre[0]].push_back(pre[1]);
        }

        for (int i=0; i<numCourses; i++) {
            if (!dfs(prerequisites, i)) return {};
        }

        return res;
    }
};
