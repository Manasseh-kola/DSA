"""
LeetCode 1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
"""

class DisjointSet:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.disconnected = n-1
        
    def find(self,node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def unite(self,node1,node2):
        root1,root2 = self.find(node1),self.find(node2)
        if root1 == root2:
            return False
        self.disconnected -=1
        if self.size[root1] < self.size[root2]:
            node1,node2 = node2,node1
        self.size[root1] += self.size[root2]
        self.root[root2] = root1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                cst= abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]) 
                edges.append((cst,i,j))
        heapq.heapify(edges)
        dS = DisjointSet(n)
        minCost = 0
        while edges and dS.disconnected != 0:
            cost,node1,node2 = heapq.heappop(edges)
            if dS.unite(node1,node2):
                    minCost+= cost
                
        return minCost
        

    
   
        
