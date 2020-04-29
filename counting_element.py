"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
 

Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""




class Solution:
    def countElements(self, lst: List[int]) -> int:
        """
        Function to get same anagrams counts
        Param:
        lst : String format for which we have to count the anagrams
        Return :
        return type will be int
        """
        
        # initializing the empty dictionary , it's like work count program
        cnt={}
        # at start we are setting count as 0 
        count = 0
        
        # applying loop to check each item if it is there or not in dictionary
        # if yes then will increment the count by 1 else will set a new key value pair
        for i in lst:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        
        # calculating the total count
        for j in cnt:
            if (j+1) in cnt:
                count += cnt[j]

        return count