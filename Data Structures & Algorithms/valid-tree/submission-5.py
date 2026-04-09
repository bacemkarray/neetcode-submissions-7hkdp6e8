class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        # need to detect a cycle
        visited = set()
        adj = {}

        for i in range(n):
            adj[i] = []
        for i,o in edges:
            adj[i].append(o)
            adj[o].append(i)
        
        def dfs(node, prev):
            if node in visited: return False
            if adj[node] == []: return True
            visited.add(node)
            for adjacent in adj[node]:
                if adjacent == prev:
                    continue
                if not dfs(adjacent, node): return False
            return True
        
        res = dfs(0, -1)
        if len(visited) != n:
            return False
        return res

        