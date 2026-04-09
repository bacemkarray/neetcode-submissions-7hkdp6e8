# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sameTree(root, subRoot):
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    if root.val != subRoot.val:
        return False
    
    left = sameTree(root.left, subRoot.left)
    right = sameTree(root.right, subRoot.right)
    return left and right



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        
        if not sameTree(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return True