# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = []
        
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            count.append(node.val)    
            traversal(node.right)
        
        traversal(root)
        return count[k-1] # array is 0 indexed
        

