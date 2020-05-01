"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""
             
             
             
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        In this we are checking what is the maximum index that we can jump from an index
        if we are able to jump till / out of the list by using maximum steps then we are good
        in case of 0  where we can't reach / eaceed zero then will retunr False
        """
        #setting intitail reach to 0 as will satrt from there only
        reach = 0
        
        # will loop through the list and in each case will take max to which we can reach 
        for i in range(len(nums)):
        
            if reach < i:
                return False
            reach = max(reach,i+nums[i])
                
        return True
                