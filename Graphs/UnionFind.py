"""
319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between 
computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, 
and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
 
"""

class Union_Find:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.size = [1 for i in range(n)]
   
        
    def findRoot(self,node):
        if self.root[node] == node:
            return node
        self.root[node] = self.findRoot(self.root[node])
        return self.root[node]
    
    def unite(self,nodeA,nodeB):
        rootA,rootB = self.findRoot(nodeA),self.findRoot(nodeB)
        if rootA == rootB:
            return False
    
        if self.size[rootA] < self.size[rootB]:
            rootA,rootB = rootB,rootA
        self.size[rootA] += self.size[rootB]
        self.root[rootB] = rootA
        
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        redundant = 0
        connected = 0
        ds = Union_Find(n)
        for nodeA,nodeB in connections:
            if ds.unite(nodeA,nodeB):
                connected +=1
            else:
                redundant +=1
            
        return n-1-connected if redundant+connected >= n-1 else -1
    
                
                
            
        
