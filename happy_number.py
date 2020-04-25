"""Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""




class Solution:
    def isHappy(self, n: int) -> bool:
    
        """Function to find happy number
        Param:
        n : Integer values that needs to be check if Happy number or not.
        Return :
        return type will be bool
        """
    
        # Taking default the number is not a happy number
        output = False
        
        # TO have the list of number which is used for checking Happy no.
        # Here will insert the calculated values to check if it is re-appearing 
        num_lst = []
        
        # WIll loop till Output is False
        while not output:
            sum = 0
            
            # Will loop after making the integer into String so that each digit/letter sqaure can be easily done
            for i in str(n):
                sum += int(i)*int(i)
            
            # will check each time if it is 100 or total sum is 1
            if sum == 1:
                return True
            #checking if the same is re-appeared , then break the loop or simple return False.
            elif sum in num_lst:
                return False
            
            # else will add them into list so that if any value re-appear then can be cheked 
            else:
                print(sum)
                num_lst.append(sum)
                n = str(sum)