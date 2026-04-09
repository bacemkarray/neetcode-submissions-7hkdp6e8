class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0,-1], [0,1], [-1,0], [1,0]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r,c) in visited or
                grid[r][c] == "0"):
                return 0

            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return 1

        for r in range(rows):
            for c in range(cols):
                islands += dfs(r,c)
                
        return islands