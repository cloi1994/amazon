class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hm = {"I" : 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        res = int(hm[s[-1]])
        
        for i in range(len(s)-2,-1,-1):
            if hm[s[i]] < hm[s[i+1]]:
                res -= hm[s[i]]
            else:
                res += hm[s[i]]
                
        return res
        
