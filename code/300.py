class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        tails = [float('-inf')] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size - 1
            
            while i < j:
                m = i + (j - i) // 2

                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
                    
            if tails[i] >= x:
                pass
            else:
                j += 1
            
            tails[j] = x
            
            if j == size:
                size += 1
        return size
                
            
