"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b"."""




class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """Function to get the  if two backspace items are equal or not
        Param:
        S , T : String format for which euality needs to be checked
        Return :
        return type will be boolean
        """
        
        # Converting String into List to perform loop and pop oprerations
        S = list(S)
        T = list(T)
        
        # will loop till the # there into the S List
        while '#' in S:
            
            # Checking if the first item is # or not , in this case no operation is needed simply remove it
            if S.index('#') != 0:
                S.pop(S.index( '#' ) - 1)
            S.remove('#')
                    
        # will loop till the # there into the T List
        while '#' in T:
        
            # Checking if the first item is # or not , in this case no operation is needed simply remove it
            if T.index('#') != 0:
                T.pop(T.index( '#' ) - 1)
            T.remove('#')
        
        # Equality check for the input string after operations
        if S == T :
            return True
        else:
            return False
        
