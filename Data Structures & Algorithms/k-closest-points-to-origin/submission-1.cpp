class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>> maxHeap;
        vector<vector<int>> res;
        for (int i=0; i<points.size(); i++) {
            int x = points[i][0];
            int y = points[i][1];
            int dist = (x*x + y*y);
            maxHeap.push({dist,x,y});
            if (maxHeap.size() > k) maxHeap.pop();
        }

        while (!maxHeap.empty()) {
            res.push_back({maxHeap.top()[1], maxHeap.top()[2]});
            maxHeap.pop();
        }

        return res;
    }
};
