#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 
        
        while right >= left:
            middle = (right + left ) // 2 
            
            if nums[middle] == target:
                return middle 
            elif nums[middle] >target:
                right = middle -1 
            elif nums[middle] < target:
                left = middle + 1 
                
        return left 
                
        
            
            
        
        
        
        
        
# @lc code=end

