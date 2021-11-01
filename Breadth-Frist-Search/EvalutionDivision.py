"""
LeetCode
130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        flip = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) in visited:
                    continue
                if board[r][c] == "O":
                    self.bfs(board,r,c,visited,flip)
        
        for currSet in flip:
            for r,c in currSet:
                board[r][c] = "X"
                
              
    def bfs(self,graph,sr,sc,visited,flip):
        R,C = len(graph),len(graph[0])
        perimeter = 0
        stack = [(sr,sc)]
        currentRegion = []
        marked = 0
        while stack:
            r,c = stack.pop()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            currentRegion.append((r,c))
            currPerimeter = 4
        
            for nr,nc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if R>nr>=0<=nc<C:
                    if graph[nr][nc] == "O":
                        currPerimeter -=1
                        stack.append((nr,nc))
                    else:
                        marked+=1
            
            perimeter +=currPerimeter
            
        if marked >= perimeter:
            flip.append(currentRegion)
    
