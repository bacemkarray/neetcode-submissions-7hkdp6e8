class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        chart = {}
        visited = set()
        for i in range(numCourses):
            chart[i] = []
        for course, prereq in prerequisites:
                chart[course].append(prereq)


        def dfs(i):
            if i in visited:
                return False
            if chart[i] == []:
                return True
            visited.add(i)
                
            for course in chart[i]:
                if not dfs(course):
                    return False
            visited.remove(i)
            chart[i] = []
            return True

        for i in chart:
            if not dfs(i):
                return False
        
        return True

        