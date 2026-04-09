class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])
        res = []
        def dfs(r,c,h,o):
            if (r < 0 or r == rows or
                c < 0 or c == cols or 
                heights[r][c] < h or
                (r,c) in o):
                return
            o.add((r,c))
            dfs(r,c+1,heights[r][c],o)
            dfs(r,c-1,heights[r][c],o)
            dfs(r+1,c,heights[r][c],o)
            dfs(r-1,c,heights[r][c],o)
            return

        for r in range(rows):
            dfs(r,0,heights[r][0],pacific)
            dfs(r,cols-1,heights[r][cols-1],atlantic)

        for c in range(cols):
            dfs(0,c,heights[0][c],pacific)
            dfs(rows-1,c,heights[rows-1][c],atlantic)

        for row in range(rows):
            for col in range(cols):
                if (row,col) in atlantic and (row,col) in pacific:
                    res.append([row,col])
        return res
