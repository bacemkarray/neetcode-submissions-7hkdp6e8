class Solution {
public:
    
    int dfs(int i, int j, vector<vector<int>>& grid) {
            int ROWS = grid.size();
            int COLS = grid[0].size();
            if (i<0 || i>=ROWS || j<0 || j>=COLS || grid[i][j] == 0) return 0;
            grid[i][j] = 0;

            return 1 + dfs(i+1,j,grid) + dfs(i-1,j,grid) + dfs(i,j+1,grid) + dfs(i,j-1,grid);
        }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        int area = 0;
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                area = max(area, dfs(i,j,grid));
            }
        }
        return area;
    }
};
