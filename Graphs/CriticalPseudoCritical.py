"""
1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1,
and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. 
A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). 
An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. 
On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:
"""

class DisjointSet:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.disconnected = n-1
        
    def findRoot(self,node):
        if self.root[node] == node:
            return node
        self.root[node] = self.findRoot(self.root[node])
        return self.root[node]
    
    def unite(self,node1,node2):
        root1,root2 = self.findRoot(node1),self.findRoot(node2)
        if root1 == root2:
            return False
        self.disconnected -=1
        if self.size[root1] < self.size[root2]:
            root1,root2 = root2,root1
        self.size[root1] += self.size[root2]
        self.root[root2] = root1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        sortEdges = sorted(enumerate(edges),key = lambda x:x[1][2])
        minTree = self.kruskal(-1,-1,n,sortEdges,edges)
        critical = []
        pseudoCritical = []
        edgePriority = [critical,pseudoCritical]
        
        for i in range(len(edges)):
            if self.kruskal(-1,sortEdges[i][0],n,sortEdges,edges) > minTree:
                critical.append(sortEdges[i][0])
            elif self.kruskal(sortEdges[i][0],-1,n,sortEdges,edges) == minTree:
                pseudoCritical.append(sortEdges[i][0])
        
        return edgePriority
        
    def kruskal(self,add,remove,n,sortEdges,edges):
        ds = DisjointSet(n)
        treeWeight = 0
        if add >=0:
            node1,node2,weight = edges[add]
            ds.unite(node1,node2)
            treeWeight+=weight
            if ds.disconnected == 0:
                return treeWeight
        
        for edge in sortEdges:
            if ds.disconnected == 0:
                break
            i = edge[0]
            node1,node2,weight = edge[1]
            if i == add or i == remove:
                continue
            if ds.unite(node1,node2):
                treeWeight+=weight
        
        return treeWeight if ds.disconnected ==0 else 1000*10000
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
