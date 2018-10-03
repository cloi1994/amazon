class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            
            mid = i + (j - i) // 2

            
            if nums[mid] == target:
                return mid
            
            #left sorted
            if nums[mid] >= nums[i]:
                
                if target >= nums[i] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
             
            #right sorted
            else:
                
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
                    
        return -1
                
                
                
