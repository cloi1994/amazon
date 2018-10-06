class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [True] + [False] * len(s)
        
        self.memo = {}
        
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    
        return dp[len(s)]
