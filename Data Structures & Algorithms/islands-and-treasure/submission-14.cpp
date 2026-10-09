class Solution {
public:
    queue<pair<int,int>> q;
    vector<pair<int,int>> directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (grid[i][j] == 0) q.push({i,j});
            }
        }

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();

            for (const auto& dir : directions) {
                int dr = curr.first + dir.first;
                int dc = curr.second + dir.second;

                if (dr>=0 && dr<ROWS && dc>=0 && dc<COLS && grid[dr][dc] == INT_MAX) {
                    q.push({dr,dc});
                    grid[dr][dc] = 1 + grid[curr.first][curr.second];
                }
            }
        }
    }
};
