class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:[] for w in words for c in w}
        res = []

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(0, min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
                if w1[:j] == w2[:j] and len(w1) > len(w2):
                    return ""

        visited = {}
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            visited[char] = False
            res.append(char)
            return False

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
            

            