class Solution(object):
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxLeft = 0
        maxRight = 0

        count = 0
        
        i = 0
        j = len(height) - 1
        
        while i < j:
            
            if height[i] < height[j]:
                if maxLeft < height[i]:
                    maxLeft = height[i]
                count += maxLeft - height[i]
                i += 1
        
            else:
                if maxRight < height[j]:
                    maxRight = height[j]   
                count += maxRight - height[j]
                j -= 1
                           
        return count
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
        
#         maxLeft = 0
#         maxRight = 0
        
#         left = [0] * len(height)
#         right = [0] * len(height)
#         count = 0
        
#         for i in range(len(height)):
#             if height[i] > maxLeft:
#                 maxLeft = height[i]
#             left[i] = maxLeft
        
#         for i in range(len(height)-1,-1,-1):
#             if height[i] > maxRight:
#                 maxRight = height[i]
#             right[i] = maxRight
            
#         for i in range(len(height)):
#             count += min(left[i],right[i]) - height[i]
            
#         return count
        
        
