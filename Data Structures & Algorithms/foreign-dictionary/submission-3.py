class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj = {}
        # rule = ""
        # res = 0
        # for word in words:
        #     for char in word:
        #         if char in adj:
        #             continue
        #         adj[char] = 0

        # def dfs(letter):
        #     nonlocal rule, res
        #     neighbor = adj[letter]
        #     if neighbor:
        #         rule = rule + neighbor
        #         dfs(neighbor)
        #         return
        #     res += 1
        #     return

        
        # for i in range(len(words)-1):
        #     for j in range(min(len(words[i]), len(words[i+1]))):
        #         if (words[i][j] != words[i+1][j] or 
        #             (words[i+1][0:len(words[i])] == words[i] and 
        #             len(words[i]) < len(words[i+1]))):
        #             adj[words[i][j]] = words[i+1][j]
        
        # rule = rule + words[0][0]
        # dfs(words[0][0])
        # if res >= 1:
        #     return ""
        # return rule
        adj = {char:set() for w in words for char in w}
        visited = {} # if value is true, its on the current path
        # if in visited and current path that means cycle -> Invalid
        res = []

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_length = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) 
                    break

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
            for neighbors in adj[char]:
                if dfs(neighbors):
                    return True
            
            visited[char] = False
            res.append(char)
            return False

        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)
                
                        
                        

