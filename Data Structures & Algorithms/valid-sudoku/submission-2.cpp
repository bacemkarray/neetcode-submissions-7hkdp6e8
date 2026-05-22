class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> rows(9);
        vector<int> cols(9);
        vector<int> blocks(9);
        int ROWS = board.size();
        int COLS = board[0].size();
        for (int r=0; r<ROWS; r++) {
            for (int c=0; c<COLS; c++) {
                if (board[r][c] == '.') continue;
                int n = board[r][c] - '0';
                int b = (r/3)*3 + (c/3);
                if (rows[r] & (1<<n) || 
                    cols[c] & (1<<n) || 
                    blocks[b] & (1<<n)) return false;
                rows[r] |= (1<<n);
                cols[c] |= (1<<n);
                blocks[b] |= (1<<n);
            }
        }
        return true;
    }
};
