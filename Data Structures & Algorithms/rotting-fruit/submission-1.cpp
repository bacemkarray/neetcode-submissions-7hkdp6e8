class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        //for every minute, we need to infect all fresh oranges that are currently adjacent to a rotten orange. 
        //multi source bfs, but its important we only increment a level every minute, not every fruit rotted
        vector<vector<int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        int fresh = 0;
        int time=0;
        int ROWS=grid.size();
        int COLS=grid[0].size();
        queue<pair<int,int>> q;

        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (grid[i][j] == 2) q.push({i,j});
                if (grid[i][j] == 1) fresh++;
            }
        }

        while (!q.empty() && fresh>0) {
            //measure how many oranges are on this current level
            int level = q.size();
            for (int i=0; i<level; i++) {
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
            time++;
        }
        return (fresh != 0) ? -1 : time;
    }
};
