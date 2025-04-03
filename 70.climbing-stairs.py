# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        end = 1 
        before_end = 1 
        
        
        for i in range(n-1):
            tmp  = end     
            end = before_end + end 
            before_end = tmp 
        return end
        
# @lc code=end

