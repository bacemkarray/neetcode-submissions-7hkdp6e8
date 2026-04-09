class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s):True}
        def dfs(i):
            if i in cache:
                return cache[i]

            for w in wordDict:
                l = len(w)
                if s[i:(i+l)] == w:
                    res = dfs(i+l)
                    if res:
                        cache[i] = True
                        return True
                    cache[i] = False
            return False
        
        return dfs(0)

        


