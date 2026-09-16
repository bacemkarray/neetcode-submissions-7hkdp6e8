class Solution {
public:
    queue<pair<int,int>> q;
    int orangesRotting(vector<vector<int>>& grid) {
        vector<vector<int>> directions = {{0,1},{0,-1},{1,0},{-1,0}};
        int res = 0;
        int fresh = 0;
        int ROWS = grid.size();
        int COLS = grid[0].size();

        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (grid[i][j] == 2) q.push({i,j});
                if (grid[i][j] == 1) fresh++;
            }
        }

        while (!q.empty() && fresh>0) {
            int snapshot = q.size();
            for (int i=0; i<snapshot; i++) {
                auto [r,c] = q.front();
                q.pop();
                for (const auto& dir : directions) {
                    int dr = r+dir[0];
                    int dc = c+dir[1];
                    if (dr>=0 && dr<ROWS && dc>=0 && dc<COLS && grid[dr][dc] == 1) {
                        q.push({dr,dc});
                        grid[dr][dc] = 2;
                        fresh--;
                    }
                }
            }
            res++;
        }
        return (fresh>0) ? -1 : res;
    }
};
