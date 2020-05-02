"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Here will be using dynamic programming
        will check for last left , right and diagonal item and will take the min of them
        if it is '1' then will increment the count and finally count*count will give the area of it
        try to eplore more and more on these problem's solution and dynamic programming
        """
        
        # setting wor and cols
        rows = len(matrix)
        
        # will check if matrix is empty of not
        if not rows:
            return 0
            
        cols = len(matrix[0])
        
        # Now will create one dynamic programming list of list in which will keep the count for the subsequent operation
        dp = [[0]*(cols+1) for _ in range(len(matrix)+1)]
        # the above will give rows+1 cross cols+1 size matrix as we need one extra for the first rows/cols as empty
        
        max_val = 0
        
        for x in range(1,rows+1):
            for y in range(1,cols+1):
                # now will check with left , right and diagonal item for min value
                
                if matrix[x-1][y-1] == '1':
                    # checking and adding 1 to it
                    dp[x][y] = min(dp[x-1][y],dp[x-1][y-1],dp[x][y-1]) + 1
                    
                max_val = max(max_val,dp[x][y])
                
        return max_val * max_val
        
        
        
        
        
        
        
        