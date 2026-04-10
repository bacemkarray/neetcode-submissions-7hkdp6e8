class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        chart = {}
        for prereq in prerequisites:
            if prereq[0] not in chart:
                chart[prereq[0]] = [prereq[1]]
            else:
                chart[prereq[0]].append(prereq[1])

        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if i not in chart:
                return True
            visited.add(i)
                
            for course in chart[i]:
                if not dfs(course):
                    return False

            visited.remove(i)
            return True

        for i in chart:
            if not dfs(i):
                return False
        
        return True

        