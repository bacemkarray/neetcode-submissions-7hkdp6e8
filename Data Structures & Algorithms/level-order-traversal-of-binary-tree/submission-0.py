# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        def bfs(node):
            if not node:
                return

            queue = collections.deque([node])
            while queue:
                level = []
                for i in range(len(queue)):
                    n = queue.popleft()
                    if n:
                        level.append(n.val)
                        queue.append(n.left)
                        queue.append(n.right) 
                if level:
                    self.levels.append(level)
        bfs(root)
        return self.levels
