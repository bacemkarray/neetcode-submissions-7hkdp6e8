class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rowSets(9);
        vector<unordered_set<char>> colSets(9);
        vector<unordered_set<char>> grids(9);
        int ROWS = board.size();
        int COLS = board[0].size();
        for (int r=0; r<ROWS; r++) {
            for (int c=0; c<COLS; c++) {
                int g = (r/3)*3 + (c/3);
                char n = board[r][c];
                if (n == '.') continue;
                if (rowSets[r].find(n) != rowSets[r].end() || colSets[c].find(n) != colSets[c].end() || grids[g].find(n) != grids[g].end()) return false;
                rowSets[r].insert(n);
                colSets[c].insert(n);
                grids[g].insert(n);
            }
        }
        return true;
    }
};
