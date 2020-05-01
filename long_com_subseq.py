"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 
If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
   Hide Hint #1  
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
   Hide Hint #2  
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Here we will be using dynamic programming whihc will dynamically assign count
        will go with diagonal previous [row][col] and take max of them
        and will keep on doing that and [-1][-1] wil have the coutn for of item which can be longestCommonSubsequence
        """
        
        # creating a dp ( dynamic programming ) list of list [][]
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        
        # adding null/blank values to initialize with 0/zero
        text1 = " " + text1
        text2 = " " + text2
        
        # Now will loop through it and do the subsequents checking
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                
                # letter eaquality check
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        return dp[-1][-1]