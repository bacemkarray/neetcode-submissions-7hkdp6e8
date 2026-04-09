class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visited = set()
        res = 1
        for i,j in edges:

            adj[i].append(j)
            adj[j].append(i)


        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            return


        for i in adj:
            if i in visited:
                continue
            dfs(i)
            if len(visited) != n:
                res += 1
            
        return res
