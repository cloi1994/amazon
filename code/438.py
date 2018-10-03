class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if not s or len(p) > len(s):
            return []
        
        pdict = [0] * 256
        sdict = [0] * 256
        
        for ele in p:
            pdict[ord(ele)] += 1
        
        
        res = []
        
        for i in range(len(p)):
            sdict[ord(s[i])] += 1
        
        if sdict == pdict:
            res.append(0)
        
        i = 0
        
        for j in range(len(p),len(s)):
            
            sdict[ord(s[j])] += 1
            sdict[ord(s[i])] -= 1
            
            if sdict == pdict:
                res.append(i+1)
            
            i += 1
            
        return res
            
            
