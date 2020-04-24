"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
	
	"""Function to find happy number
    Param:
    nums : List format input , numbers to be checked
    Return :
    return type will be int
    """
    
        # setting the 1st element as maximum value as we have to find the maximum 
        max = nums[0]
        
        # taking sum as fist value in case of sinle item into the list
        sum = nums[0]
        
        # Looping into the list except 1st element as we have taken the same earlier for initialization 
        for n in nums[1:]:
        
            # checking if the next item is greater then sum if yes them will set sum as thet itmem's value
            if n > sum + n:
                sum = n
            
            # else will do the regular sum for getting max value
            else:
                sum = sum + n
            # will return the max value b/w sum and max
            if sum > max:
                max = sum
        return max