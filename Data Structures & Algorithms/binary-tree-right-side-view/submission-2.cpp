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
    vector<int> res;
    unordered_set<int> levels;

    void dfs(TreeNode* node, int level) {
        if (levels.find(level) == levels.end()) {
            res.push_back(node->val);
            levels.insert(level);
        } 
        if (node->right != nullptr) dfs(node->right, level+1);
        if (node->left != nullptr) dfs(node->left, level+1);
    }

    vector<int> rightSideView(TreeNode* root) {
        res = {};
        levels = {};
        if (root==nullptr) return res;
        dfs(root, 0);
        return res;
    }
};
