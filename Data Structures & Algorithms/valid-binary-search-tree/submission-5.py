# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def islocalBST(node, left, right):
    if not node:
        return True
    
    if not left < node.val < right:
        return False
    
    left = islocalBST(node.left, left, node.val)
    right = islocalBST(node.right, node.val, right)
    return left and right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return islocalBST(root, float("-inf"), float("inf"))

        