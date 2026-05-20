class Solution {
public:
    vector<pair<int,int>> directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    void dfs(vector<vector<int>>& grid, int i, int j, int distance) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        if (i<0 || i>=ROWS || j<0 || j>=COLS || grid[i][j] < 0) return;
        if (distance > 0 && grid[i][j] <= distance) return;
        grid[i][j] = distance;
        for (const auto& [row, col] : directions) {
            int ni = i + row;
            int nj = j + col;
            dfs(grid, ni, nj, distance+1);
        }
        
    }


    void islandsAndTreasure(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (grid[i][j] == 0) dfs(grid,i,j,0);
            }
        }
    }
};
