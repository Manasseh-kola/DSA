"""
LeetCode
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable. You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjList = {}
        index = 0
        for from_,to in equations:
            weight = values[index]
            if from_ not in adjList:
                adjList[from_] = []
            if to not in adjList:
                adjList[to] = []
           
            adjList[from_].append((to,weight))
            adjList[to].append((from_,1/weight))
               
            index+=1
            
        
        result = []
        for start,end in queries:
            
            if start not in adjList and end not in adjList:
                result.append(-1)
            
            elif start == end:
                result.append(1)
            else:
                visited = set()
                productArray = []
                self.depthFirst(start,start,end,adjList,1,visited,productArray)
                if len(productArray):
                    result.append(productArray[0])

                else:
                    result.append(-1)
                
        
        return result
    
    def depthFirst(self,start,currentNode,end,adjList,product,visited,productArray):
        
        if currentNode in visited:
            return
        visited.add(currentNode)
        if currentNode == end:
            productArray.append(product)
            return
       
        if currentNode not in adjList:
            return 
        
        for branch in adjList[currentNode]:
            if len(productArray):
                break
            branchNode,currentWeight = branch
            newProduct = product*currentWeight
            self.depthFirst(start,branchNode,end,adjList,newProduct,visited,productArray)
    
