"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(n):
            new_n = Node(n.val)
            visited[n] = new_n

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    new_neighbor = dfs(neighbor)
                    new_n.neighbors.append(new_neighbor)
                else:
                    new_n.neighbors.append(visited[neighbor])
            
            return new_n
        
        if not node:
            return None

        return dfs(node)

