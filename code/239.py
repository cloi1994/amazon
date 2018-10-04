from heapq import heappush, heappop, nsmallest

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        pq = []
        
        res = []
        
        i = 0
        
        for j in range(len(nums)):
        
            heappush(pq,-nums[j])
                
            if len(pq) == k:
                res.append(-nsmallest(1,pq)[0])
            
            if len(pq) >= k:
                pq.remove(-nums[i])
                i += 1
                
        return res
        
