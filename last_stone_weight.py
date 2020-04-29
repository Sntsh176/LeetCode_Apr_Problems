"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Function to get last heaviest stone ( element's values for the given list )
        Param:
        stones : List value , unordered 
        Return :
        return type will be int which will be the maximum item's value
        """
        
        # initial weight for the first 2 elements
        a = 0
        b = 0
        
        # will loop till list have item , if no item then will return 0 as else stmt of the loop
        while stones:
            
            # checking if the list is with one item ( initially / after doing pop )
            if len(stones) == 1:
                return stones[0]
                
            # sorting the list in ascending order as pop operation will delete heaviest stone 
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            
            # checking if 2 pop items are same ? , otherwise 
            # append ( a-b ) as a > b cause we have already sorted the list
            if a == b:
                if stones:
                    continue
            else:
                stones.append( a - b)
                
        # if List with no values then return 0
        else:
            return 0