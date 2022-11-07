class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Mapping prerequisites
        prerMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prerMap[course].append(prereq)

        # Check if it is visited
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            elif prerMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in prerMap[crs]:
                if not dfs(pre):return False
            visitSet.remove(crs)
            prerMap[crs] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False

        return True  