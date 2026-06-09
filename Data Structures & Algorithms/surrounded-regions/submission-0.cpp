class Solution {
public:
    void dfs(vector<vector<char>>& board,int i, int j) {
        // if you come across in the dfs an edge piece return false
        if (i<0 || i>=board.size() || j<0 || j>=board[0].size() || board[i][j] != 'O') return;
        board[i][j] = 'T';
        dfs(board,i+1,j);
        dfs(board,i-1,j);
        dfs(board,i,j+1);
        dfs(board,i,j-1);
    }

    void solve(vector<vector<char>>& board) {
        int ROWS = board.size();
        int COLS = board[0].size();
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (board[i][j] == 'O' && 
                ((i==0 || i==ROWS-1) ||
                (j==0 || j==COLS-1))) dfs(board,i,j);
            }
        }

        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
            }
        }
        
        for (int i=0; i<ROWS; i++) {
            for (int j=0; j<COLS; j++) {
                if (board[i][j] == 'T') board[i][j] = 'O';
            }
        }
    }
};
