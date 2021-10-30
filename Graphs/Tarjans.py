"""
Leet code 1192. Critical Connections in a Network
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a 
connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        lowlink = [-1 for i in range(n)]
        network = [[] for _ in range(n)]
        for a, b in connections:
            network[a].append(b)
            network[b].append(a)
        
        def tarjan(prev,node,time,lowlink,network,bridge):
            if lowlink[node] != -1:
                return lowlink[node]

            lowlink[node] = time
            for child in network[node]:
                if child != prev:
                    newLow = tarjan(node,child,time+1,lowlink,network,bridge)
                    lowlink[node] = min(lowlink[node],newLow)
                    if lowlink[child] > time:
                        bridge.append([child,node])    
            return lowlink[node]
        
        bridge = []
        tarjan(0,0,0,lowlink,network,bridge)
        return bridge
