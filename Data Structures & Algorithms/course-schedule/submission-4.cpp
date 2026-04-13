class Solution {
        unordered_map<int, vector<int>> adjList;
        unordered_set<int> visiting;
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        for (int i=0; i<numCourses; i++) {
            adjList[i] = {};
        }
        for (auto& prereq : prerequisites) {
            adjList[prereq[0]].push_back(prereq[1]);
        }
        for (int i=0; i<numCourses; i++) {
            if (!dfs(i)) { return false; }
        }
        return true;
    }

    bool dfs(int crs) {
        if (visiting.count(crs)) { return false; }
        if (adjList[crs].empty()) { return true; }
        visiting.insert(crs);
        for (int pre : adjList[crs]) {
            if (!dfs(pre)) { return false; }
        }
        visiting.erase(crs);
        adjList[crs].clear();
        return true;
    }
};
