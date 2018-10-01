class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        add = 1
        
        
        for i in range(len(s)-1,-1,-1):
            res +=  add * (ord(s[i]) - ord('A') + 1)
            add *= 26
        return res
            
        
        
        
