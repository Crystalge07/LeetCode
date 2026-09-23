# May 9, 2026

class Solution(object):
    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str]
        :rtype: str
        """

# check the list is non empty
# go through all elements and check first index
# call recursively

        result = ""
        length = len(strs)
        if length == 0: #base case
            return result

        for i in range (0, length):
            value = strs[i]
            if not value:
                return result
        
        prefix = strs[0][0]
        value = strs[0][0]
        for i in range (0, length): # goes through all elements
            if strs[i][0] != prefix:
                return result
            else: strs[i] = strs[i][1:]
        
        result = result+value
        
        return value + self.longestCommonPrefix(strs)
            

            