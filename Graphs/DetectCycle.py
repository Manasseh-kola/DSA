"""
Given an Adjacency list-edges, return a boolean indicating wether the graph contains a cycle.
"""
def cycleInGraph(edges):
    visited = [False for _ in range(len(edges))]
    inStack = [False for _ in range(len(edges))]
    for i in range(len(edges)):
      if visited[i]:
        continue

      isCyclic = traverseGraph(visited,inStack,edges,i)
      if isCyclic:
        return True

    return False
		
	
def traverseGraph(visited,inStack,edges,currentNode):
	visited[currentNode] = True
	inStack[currentNode] = True
	
	
	for adjacentNode in edges[currentNode]:
		if not visited[adjacentNode]:
			isCyclic = traverseGraph(visited,inStack,edges,adjacentNode)
			if isCyclic:
				return True
		elif inStack[adjacentNode]:
			return True
		
	inStack[currentNode] = False
	
	return False
