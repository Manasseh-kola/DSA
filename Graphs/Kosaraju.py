"""
Given a list of airports (three-letter codes like "JFK" ), a list of routes (one-way flights from one airport to another like ["JFK", "SFO"] ), and a starting airport.
Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order for someone to be able to reach any airport in
the list, starting at the starting airport. Note that routes only allow you to fly in one direction; for instance, the route ["JFK", "SFO"] only allows you to fly from "JFK"
to "SFO" . Also note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting airport by stopping at other airports first.

Test Case
airports = [
 "BGI", "CDG", "DEL", "DOH", "DSM",
 "JFK", "LGA", "LHR", "ORD", "SAN",
]
routes = [
 ["DSM", "ORD"],
 ["ORD", "BGI"],
 ["BGI", "LGA"],
 ["SIN", "CDG"],
 ["CDG", "SIN"],
 ["CDG", "BUD"],
 ["DEL", "DOH"],
 ["DEL", "CDG"],
 ["TLV", "DEL"],
 ["EWR", "HND"],
 ["HND", "ICN"],
 ["HND", "JFK"],
 ["ICN", "JFK"],
 ["JFK", "LGA"],
 ["EYW", "LHR"],
 ["LHR", "SFO"],
 ["SFO", "SAN"],
 ["SFO", "DSM"],
 ["SAN", "EYW"],
]
startingAirport = "LGA"

Ouput 
3

"""

def airportConnections(airports, routes, startingAirport):
    adjList = {}
    reversedList = {}
    inDegree = {airport:0 for airport in airports}
    adjList = {airport:[] for airport in airports}
    #Reversed adjaceny list prevents component leakage
    reversedList = {airport:[] for airport in airports}

    for start,destination in routes:
      adjList[start].append(destination)
      reversedList[destination].append(start)

    visited = set()
    finishTimes = postOrderTraverse(adjList,visited)
    root,componentGraph = sccs(reversedList,finishTimes)

    for start,destination in routes:
      if root[start] != root[destination]:
        inDegree[destination] +=1

    minNumber = 0
    for component in componentGraph:
      if startingAirport in component:
        continue
      isZeroDegree = True
      for node in component:
        if inDegree[node] !=0:
          isZeroDegree = False
          break
      if isZeroDegree:
        minNumber +=1

    return minNumber
			
def sccs(reversedList,finishTimes):
	visited = set()
	componentGraph = []
	roots = {}
	
	def findComponents(node,currentSet,root):
		visited.add(node)
		currentSet.add(node)
		roots[node] = root
		for childNode in reversedList[node]:
			if childNode not in visited:
				findComponents(childNode,currentSet,root)
	
	for node in reversed(finishTimes):
		currentSet = set()
		if node not in visited:
			findComponents(node,currentSet,node)
			componentGraph.append(currentSet)
			
	return (roots,componentGraph)
	
def postOrderTraverse(adjList,visited):
	postOrder = []
	def search(currentNode):
		visited.add(currentNode)
		for childNode in adjList[currentNode]:
			if childNode not in visited:
				search(childNode)
		postOrder.append(currentNode)
	
	for node in adjList:
		if node not in visited:
			search(node)
			
	return postOrder
