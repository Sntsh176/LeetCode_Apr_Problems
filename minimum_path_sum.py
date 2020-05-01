"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Function to get same island count
        Param:
        grid : list of list 
        Return :
        return type will be int , total path cost ( minimum )
        """
        
        # checking if the grid is empty ?
        if not grid:
            return 0
        
        # no of the rows
        m = len(grid)
        
        # vertical length of the grid | columns
        n = len(grid[0])       
        
            
        # Now in order to find the minimum path will keep on adding last value ( m-1 / n-1 ) 
        # after that will check from the adjacent rows/columns for the minimum
        # and then will update the grid for that position with the miimum value after comparing
        
        # first will do 1st row and column as these are boundary 
        #after that will apply loop to chheck the minimum with adjacent
        for i in range(1, n):
            # row wise operation for 1st row 2nd column onwards adding with previous value
            grid[0][i] += grid[0][i-1]
        
        # now will do same for 1st column
        for i in range(1, m):
            # column wise operation for 1st col 2nd row onwards adding with previous value
            grid[i][0] += grid[i-1][0]
            
        # the below loops are for checking with previous adjacent rows/columns
        # will take the minimum of them and will assign minimum value to that position of grid matrix
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j] , grid[i][j-1])
                
                
        return grid[-1][-1]