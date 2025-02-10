# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_position = 0 
        
        for index in range(1, len(nums)):
            
            if nums[index] !=  nums[unique_position]:
                
                unique_position+= 1 
                nums[unique_position] = nums[index]
        return unique_position + 1 
            
            
        
        
# @lc code=end

