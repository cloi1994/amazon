class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        i = 0
        j = len(nums) - 1
        
        while i < j:
            
            mid = i + (j - i) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        
        if nums[i] >= target:
            return i
        return i+1
            
        
