class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        prereq = {c:[] for c in range(numCourses)}
        output = []
        visit, cycle = set(), set()

        for cs, pre in prerequisites:
            prereq[cs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False: return []

        return output