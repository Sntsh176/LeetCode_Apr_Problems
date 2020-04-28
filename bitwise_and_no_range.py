"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Here will take the approach of bit shift , for a given range will do the right shift till m<n
        otherwise will break / get out of the loop
        and in each loop will increment the count for which later will do the left shift
        """
        
        # setting coutn variable 
        count = 0
        
        while m < n:
            m = m >> 1
            n = n >> 1
            count += 1
            
        return m << count