"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Function to get same anagrams counts
        Param:
        strs : String format for which we have to count the anagrams
        Return :
        return type will be list of items with similar anagram and its values
        """
        
        # Count dictionary to deal with similar anagrams ( having same letters )
        cnt={}
        
        # Now looping through the strs 
        for string in strs:
            
            # every time we are sorting it and then same anagrams are getting evaluated
            # and we are adding them into the dictionary
            s=''.join(sorted(string))
            if s in cnt:
                cnt[s].append(string)
            else:
                cnt[s]=[string]
                
        # returning the values of the dictionary as these will be having same anagrams values.
        return (cnt.values())

