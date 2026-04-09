class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]


            for w in wordDict:
                l = len(w)
                if s[i:(i+l)] == w:
                    res = dfs(i+l)
                    if res:
                        return True
                    cache[i] = res
            return False
        
        return dfs(0)

        


