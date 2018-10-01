class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = ""
        
        while n:
        
            res = chr(n % 26 - 1 + ord('A')) + res
            n -= 1
            n /= 26
            
        return res
        
