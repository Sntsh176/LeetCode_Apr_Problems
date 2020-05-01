"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
            
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Function to get same island count
        Param:
        strs : list of list 
        Return :
        return type will be int , number of islands
        """
        
        # checking if the input / grid list is empty then return 0
        if len(grid) == 0:
            return 0
        
        # nested function could have been outside also
        def dfs_island(matrix , x , y , r , c):
            """
            Defining the recursive function to check the adjacent | horizontally and vertically
            Param
            matrix : list of list
            x : rows position
            y : column position
            r : total horixontal length
            c : total vertical length
            """
            
            # checking if the adjacent are 0 or not if not then go on checking further to find an island
            if x < 0 or x >= r or y < 0 or y >= c or matrix[x][y]!= '1':
                return
                
            # setting value as '2' for already scrolled / checked rows/columns
            matrix[x][y] = '2'
            
            # now will recusively call for all four direction of adjacent values check
            dfs_island(matrix,x+1,y,r,c)
            dfs_island(matrix,x,y+1,r,c)
            dfs_island(matrix,x-1,y,r,c)
            dfs_island(matrix,x,y-1,r,c)
        
        # setting initial count for the islands
        no_island = 0
        
        # no. of rows of the grid 
        rows = len(grid)
        #print(rows)
        
        # vertical length of the grid
        cols = len(grid[0])
        #print(cols)

        # as this is 2D list so two loops are applied here
        for i in range(rows):
            for j in range(cols):

                # if the value is 1 check for adjacent rows/columns
                if grid[i][j] == '1':
                    # if yes then call the recursive function
                    dfs_island(grid , i , j , rows , cols)
                    no_island += 1
        
        # and finally return the islands count
        return no_island
    