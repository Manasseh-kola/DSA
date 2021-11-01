"""
210. Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
"""

#Kahns Algorithm

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        inDegrees = {}
        topologicalSort = []
        for edge,node in prerequisites:
            if node not in adjList:
                adjList[node] = []
            adjList[node].append(edge)
            inDegrees[edge] = inDegrees.get(edge,0)+1
            
        zeroInDegrees = deque([i for i in range(numCourses) if i not in inDegrees])
        
        while zeroInDegrees:
            node = zeroInDegrees.popleft()
            topologicalSort.append(node)
            if node not in adjList:
                continue
            for child in adjList[node]:
                inDegrees[child] -=1
                if inDegrees[child] == 0:
                    zeroInDegrees.append(child)
        
        return topologicalSort if len(topologicalSort)== numCourses else []
            
        
