# @before-stub-for-debug-begin
from python3problem27 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique = -1 
        
        for index, num in enumerate(nums) :
            
            if num != val :
                unique+=1 
                nums[unique] = num 
        
        return unique +1 
        
                
        
# @lc code=end

