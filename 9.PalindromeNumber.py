# May 6, 2026

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        string = str(x)
        
        if len(string) <= 1:
            return True
        if string[0] != string[-1]:
            return False
        
        return self.isPalindrome(string[1:-1])