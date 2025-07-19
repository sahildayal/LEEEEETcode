'''
1091. Shortest Path in a Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        q.append((0,0))
        visit.add((0,0))

        length = 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                
                directions = [[1,0], [-1,0], [0,1], [0,-1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in directions:
                    if (0<=(r+dr)<n and 0<=(c+dc)<n and (r+dr, c+dc) not in visit and grid[r+dr][c+dc] == 0):
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))

            length+=1
        return -1