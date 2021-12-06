import heapq
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    # Write your code here.
	nodes = [[Nodes(r,c) for c in range(len(graph[r]))] for r in range(len(graph))]
	R,C = len(graph),len(graph[0])
	startNode = nodes[startRow][startCol]
	endNode = nodes[endRow][endCol]
	startNode.G = 0
	heap = [(0,startRow,startCol)]
	heapq.heapify(heap)
	
	while len(heap):
		_,r,c = heapq.heappop(heap)
		if (r,c) == (endRow,endCol):
			return buildPath(endNode)
		
		currNode = nodes[r][c]
		for nr,nc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
			if C>nc>=0<=nr<R:
				if graph[nr][nc] == 1:
					continue
				nextNode = nodes[nr][nc]
				nextG = currNode.G+1
				if nextG >= nextNode.G:
					continue
				nextNode.G = nextG
				nextNode.H = abs(endRow-nr)+abs(endCol-nc)
				nextNode.parent = currNode
				heapq.heappush(heap,(nextNode.G+nextNode.H,nr,nc))
	return []
		
def buildPath(currNode):
	path = []
	while currNode is not None:
		path.append([currNode.row,currNode.col])
		currNode = currNode.parent
	return path[::-1]
	
class Nodes:
	def __init__(self,row,col):
		self.row = row
		self.col = col
		self.G = float("inf")
		self.H = float("inf")
		self.parent = None
