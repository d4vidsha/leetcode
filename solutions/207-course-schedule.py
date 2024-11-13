class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        for fromSubj, toSubj in prerequisites:
            adjList[fromSubj].append(toSubj)
        visited = set()
        def dfs(course):
            if course in visited:
                # this is a cycle
                return False
            if adjList[course] == []:
                return True
            visited.add(course)
            for c in adjList[course]:
                if dfs(c) == False:
                    return False
            visited.remove(course)
            adjList[course] = [] 
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
