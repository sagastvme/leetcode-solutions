# @before-stub-for-debug-begin
from python3problem268 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0 
        target = 0 
        for i in nums:
            total+= i
        for i in range(len(nums)+1):
            target +=i
        return target - total
        
        
# @lc code=end

