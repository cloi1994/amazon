class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sset = set()
        
        i = 0
        
        res = 0
        
        for j in range(len(s)):
            while s[j] in sset:
                sset.remove(s[i])
                i += 1
            res = max(j-i+1,res)
            sset.add(s[j])
            
        return res
                
        
