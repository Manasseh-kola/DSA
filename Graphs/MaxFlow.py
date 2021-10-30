
"""
Ford-Fulkerson algorithm with
Edmonds-Karp optimization
"""

from collections import deque

def bfs(residualCapacity,source,sink):
    queue = deque([source])
    visited = set()
    parents = {}
    isAugmenting = False

    while len(queue):
        u = queue.popleft()
        visited.add(u)
        for v in range(len(residualCapacity)):
            if v not in visited and residualCapacity[u][v] >0:
                parents[v] = u
                queue.append(v)
                if v == sink:
                    isAugmenting = True
                    break
    return (isAugmenting,parents)


def maxflow(capacity,source,sink):
    residualCapacity = capacity
    maxFlow  = 0
    while True:
        isAugmenting, parent = bfs(residualCapacity,source,sink)
        if not isAugmenting:
            break

        flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            if residualCapacity[u][v] < flow:
                flow = residualCapacity[u][v]
            v = u
        maxFlow +=flow
        v = sink
        while v != source:
            u = parent[v]
            residualCapacity[u][v] -=flow
            residualCapacity[v][u] +=flow
            v = u

        

    return maxFlow

capacity = [[0,0,0,0,0,0,0],
            [0,0,6,0,9,0,0],
            [0,0,0,6,0,0,0],
            [0,0,0,0,0,9,5],
            [0,0,6,0,0,4,0],
            [0,0,0,0,0,0,3],
            [0,0,0,0,0,0,0]
            ]
source =1
sink = 6
maximumFlow = maxflow(capacity,source,sink)
print(maximumFlow)

