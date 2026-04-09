class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key is dependency
        # values is a list of courses that depend on it
        adjList = {}
        visited = set()

        for i in range(numCourses):
            adjList[i] = []
        
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        


        
        def dfs(c):
            if c in visited:
                return False
            if adjList[c] == []:
                return True
            
            visited.add(c)
            for p in adjList[c]:
                if not dfs(p): return False
            visited.remove(c)
            return True

            
        for course in range(numCourses):
            if not dfs(course): return False
        return True
                
                



        
        
    
        # dfs(prerequisite[i][0], prerequisite[i][1])
        # if index 1 of preq[i] in the hashmap
        # hashmap[preq[i][1]].append(preq[i][0])
        # else
        # hashmap[preq[i][1]] = [preq[i][0]]


