class Solution {
public:
    int const INF = 2147483647;
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int directions[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        queue<pair<int,int>> q;   
        int ROWS = grid.size();
        int COLS = grid[0].size();
        int distance = 0;
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (grid[i][j] == 0) q.push({i,j});
            }
        }
        
        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            for (const auto& [row, col] : directions) {
                int nr = r + row;
                int nc = c + col;

                if (nr>=0 && nr<ROWS && nc>=0 && nc<COLS && grid[nr][nc] == INF) {
                    grid[nr][nc] = grid[r][c]+1;
                    q.push({nr,nc});
                }
            }
        }
        return;
    }
};
