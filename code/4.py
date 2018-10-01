class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        left = 0
        right = len(nums1) 
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        while left <= right:
            cut1 = left + (right - left) // 2
            cut2 = (n1+n2) / 2 - cut1
            
            L1 = nums1[cut1-1] if cut1 !=0 else float('-inf')
            R1 = nums1[cut1] if cut1 !=n1 else float('inf')
            L2 = nums2[cut2-1] if cut2 !=0 else float('-inf')
            R2 = nums2[cut2] if cut2 !=n2 else float('inf')
            
            if L1 > R2:
                right = cut1 - 1
            elif L2 > R1:
                left = cut1 + 1
            else:
                
                if (n1 + n2) % 2 == 1:
                    return min(R1,R2)
                else:
                    return (max(L1,L2) + min(R1, R2)) / 2.0
                    
            
        return -1
                    
        
