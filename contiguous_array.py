"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""



class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        sum = 0
        longest = 0
        my_dict = {0:-1}
        for index , num in enumerate(nums):
            if num == 0:
                sum += 1
            else:
                sum -= 1
                
            if sum in my_dict.keys():
                longest = max( longest , index - my_dict[sum])
            else:
                my_dict[sum] = index
                
        return longest
                