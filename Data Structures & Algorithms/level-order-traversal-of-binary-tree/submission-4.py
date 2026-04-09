# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = collections.deque([root])
        levels = []
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    level.append(curr.val)
            if level:
                levels.append(level)

        return levels


            

        
        
        