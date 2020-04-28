"""Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Function to get the maximum path / diameter of a Tree Node
        Param:
        root : Tree Object 
        Return :
        return type will be int which will be the maximum path of the Tree Node
        """
        # initializing with 0 as if no Node left/right then length / path will be zero
        self.diameter = 0
        
        # defining a function which will be called recursively to find the left and right branches of the Tree Node
        def getDiameter(node):
            # returning zero / 0 if the recursive call ends with None pointer ( left / right )
            if not node: 
                return 0

            # Now setting the left / right branches length 
            l, r = getDiameter(node.left), getDiameter(node.right)
            
            # will take max of recursively calculated diameter
            self.diameter = max(self.diameter, l+r)
            
            # This return is needed for recursive calculation 
            return max(l, r)+1 #add the node it self

        if not root: 
            return self.diameter
        
        # Just to call the recursive function 
        getDiameter(root)

        return self.diameter