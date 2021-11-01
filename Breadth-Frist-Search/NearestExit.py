"""
1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        visited = set()
        queue = deque([((entrance[0],entrance[1]),0)])
        R = len(maze); C = len(maze[0])
        minSteps = float("inf")
        
        while len(queue):
            index,depth = queue.popleft()
            r,c = index
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if depth>minSteps:
                continue
            if r==R-1 or r==0 or c==0 or c == C-1:
                if depth < minSteps:
                    if depth !=0:
                        minSteps = depth
            
            for ar,ac in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if R>ar>=0<=ac<C:
                    if (ar,ac) not in visited:
                        if maze[ar][ac] == ".":
                            queue.append(((ar,ac),depth+1))
                            
        return minSteps if minSteps!= float("inf") else -1
