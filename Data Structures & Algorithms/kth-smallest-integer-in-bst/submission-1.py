# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        # should be [2, 3, 4, 5]
        def traversal(node):
            if not node:
                return

            left = traversal(node.left)
            nodes.append(node.val)
            right = traversal(node.right)
            
        
        traversal(root)
        return nodes[k-1]
