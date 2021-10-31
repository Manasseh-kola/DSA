import heapq
#start-starting node, edges-adjList
def dijkstrasAlgorithm(start, edges):
    minDistances = [float("inf") for _ in range(len(edges))]
    minDistances[start] = 0
      minHeap = []
    heapq.heappush(minHeap,(0,start))

    while len(minHeap):
      currentMinDistance,currentNode = heapq.heappop(minHeap)
      if currentMinDistance == float("inf"):
        break
      for edge in edges[currentNode]:
        childNode,distance = edge
        newDistance = currentMinDistance + distance
        prevDistance = minDistances[childNode]
        if newDistance < prevDistance:
          minDistances[childNode] = newDistance
          heapq.heappush(minHeap,(newDistance,childNode))
    # min distance = -1 if node is unreachable
    return list(map(lambda x: -1 if x == float("inf") else x,minDistances))
