from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[prereq] += 1
            adj[course].append(prereq)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            for prereq in adj[course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)

        return finish == numCourses

