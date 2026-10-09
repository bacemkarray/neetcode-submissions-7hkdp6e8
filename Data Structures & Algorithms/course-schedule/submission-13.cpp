class Solution {
public:
    unordered_map<int,vector<int>> adj;
    unordered_set<int> visited;
    bool dfs(vector<vector<int>>& prerequisites, int crs) {
        if (adj[crs].empty()) return true;
        if (visited.contains(crs)) return false;
        visited.insert(crs);

        for (const auto& prereq : adj[crs]) {
            if (!dfs(prerequisites, prereq)) return false;
        }
        visited.erase(crs);
        adj[crs] = {};
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i=0; i<prerequisites.size(); i++) {
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        for (int i=0; i<numCourses; i++) {
            if (!adj[i].empty()) {
                if (!dfs(prerequisites, i)) return false;
            }
        }
        return true;
    }
};
