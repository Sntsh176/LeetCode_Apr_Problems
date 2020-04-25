class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using 2 pointers where 1st one will have the satrt index and other one will have the end index of the list
        # Setting start at 0
        i = 0 
        j = len(nums) - 1
        
        # Now will loop till the right index is greater than the left index
        while (i < j):
            # if the value for the index is zero then will delete it else will skip that item of the list
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(j,0)
                j -= 1
                
            else:
                i += 1