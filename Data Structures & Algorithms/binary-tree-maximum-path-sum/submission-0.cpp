/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    int res = INT_MIN;
public:
    int dfs(TreeNode* node) {
        if (node == nullptr) return 0;

        int left = max(0,dfs(node->left));
        int right = max(0,dfs(node->right));
        
        res = max(res, node->val+left+right);
        
        return node->val + max(left,right);
    }


    int maxPathSum(TreeNode* root) {
        dfs(root);
        return res;
    }
};
