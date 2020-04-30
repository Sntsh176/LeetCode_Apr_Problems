"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
   Hide Hint #1  
Will Brute force work here? Try to optimize it.
   Hide Hint #2  
Can we optimize it by using some extra space?
   Hide Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?
   Hide Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
"""



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Param:
        nums : List of items
        k : the sum value which needed to be find in count using subarray
        return:
        return type will be int , count 
        """
        # The approach here is to calculate the sum of each item in one loop of list and store the sum into dictionary
        # we will check if the item of list ,sum and sum - k is equal to k or not 
        # This will confirm th count of subarray
        
        sum_dict = {0:1}
        # here we have taken one entry in dictionary as if sum - k = 0 this means there is a subarray whose sum = k
        sum = 0
        # initializing count variable
        count = 0
        
        # now will loop with each item and parallely will calculate the sum and store the same into the dictionary
        for num in nums:
            sum += num
            if sum-k in sum_dict:
                count += sum_dict[sum-k]
            if sum in sum_dict:
                sum_dict[sum] += 1
            else:
                sum_dict[sum] = 1
                
                
        return count
            