"""

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5

 

Constraints:

    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100

"""


from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumDiagonal1 = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if len(mat) <= 1:
                    return mat[i][j]
                elif i == j or i + j == len(mat)-1:
                    sumDiagonal1 += mat[i][j]
        return sumDiagonal1
                # elif i + j == len(mat)-1:
                #     sumDiagonal2 += mat[i][j]
                # print(mat[i][j])


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]
       ]

mat3 = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
"""
3-1-0 < 3
3-1-1 <1 1 < 1
3-1-2 < 0

"""
mat2 = [[5]]
sum = Solution().diagonalSum(mat3)
print(f"sum of diagonal two : {sum}")