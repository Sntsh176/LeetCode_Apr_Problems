"""Problem Statement

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        """Function to get the non duplicate item
        Param:
        nums : List format input , numbers to be checked
        Return :
        return type will be int
        """
    
        # Here we are taking Dictionary which will havevalues as key
        dict = {}
        
        #Now looping with the entire List
        for i in nums:
            # will check if the key is already there if not then
            # make an entry into the Dictionary
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
                
        #This is to get the non - duplicate item
        for i in dict:
            if dict[i] == 1:
                return i   
