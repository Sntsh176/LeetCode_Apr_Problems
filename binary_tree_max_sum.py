"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum_val = -math.inf
        
        # Now will call the maxSum method recursively
        self.maxSum(root)
        return self.max_sum_val
        

    def maxSum(self , node):
        # this is for recursive call when we reach to the leaf ( there won't be any left/right node for it)
        # this is not to check the initial root check cause it already confirmed root is Non- empty  
        if not node:
            return 0
            
        # we are keeping the values for left leaf and right leaf
        left = max(0 , self.maxSum(node.left))
        right = max(0 , self.maxSum(node.right))
        
        # here we are keeping the max which will be return as maximum sum
        self.max_sum_val = max(self.max_sum_val, left+right+node.val)
        # returning the below for recursive operation 
        return max(left,right) + node.val