"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""



# this is the typical case of binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Here the same problem can be solved by finding pivot element but that will cause 2 time binary search 
        time complexity 2Log(n)
        so to avoid it will go for binary search directly as will have atleast one half in acesnding order
        Param
        nums : list of item in ewhich we have to search
        target : return type int , index value of from the pivot list 
        """
        
        # checking if the list is empty ?
        if not nums:
            return -1
        
        # for binary search low , high  and mid are needed
        low = 0
        high = len(nums)-1
        # as mid will be updated we can keep any value , let's have None for now
        mid = None 
        
        # applying while loop 
        while low <= high:
            # will find the mid value and compare with the value whcih needs to be searched
            mid = (low + high)//2 # floor division
            
            # checking for the search value with mid
            if target == nums[mid]:
                return mid
            
            # if mid is not the value then will start narrowing down the value
            # if values is in sorted part of the list
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                
                else:
                    low = mid + 1
                    
            # if values is not in sorted part of the list
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid - 1
                    
        # otehrwise return -1 if not found
        return -1
                    