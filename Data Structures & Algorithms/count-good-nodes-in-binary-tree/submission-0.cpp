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
public:
    int res;
    void dfs(TreeNode* node, int greatest) {
        if (node == nullptr) return;
        if (node->val >= greatest) res+=1;
        if (node->left) dfs(node->left, max(node->val,greatest));
        if (node->right) dfs(node->right, max(node->val,greatest));
    }

    int goodNodes(TreeNode* root) {
        res = 0;
        dfs(root,root->val);
        return res;
    }
};
