'''
SEARCH A 2d Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

# time complexity: O(mlogn)
from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        L = 0
        R = len(matrix[i])-1

        while L <= R:
            mid = (L+R)//2
            if target > matrix[i][mid]:
                L = mid+1
            elif target < matrix[i][mid]:
                R = mid-1
            else:
                return True
    return False

# time complexity O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L = 0
        H = m*n-1

        while L <= H:
            mid = (L+H)//2
            row = mid // n
            column = mid%n
            val = matrix[row][column]

            if target > val:
                L = mid + 1
            elif target < val:
                H = mid - 1
            else:
                return True
        
        return False
    
