"""
LeetCode
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island 
(i.e., one or more connected land cells).The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        perimeter = [0]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    continue
                if (r,c) not in visited:
                    self.bfs(visited,grid,r,c,perimeter)
                    return perimeter[0]
                    
        return 0
                    
    def bfs(self,visited,graph,sr,sc,perimeter):
        R = len(graph)
        C = len(graph[0])
        stack = [(sr,sc)]
        
        while stack:
            r,c = stack.pop()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            currPerimeter = 4
            for nr,nc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if R>nr>= 0 <=nc<C:
                    if graph[nr][nc] !=0:
                        currPerimeter -=1
                        stack.append((nr,nc))

            perimeter[0]+= currPerimeter
