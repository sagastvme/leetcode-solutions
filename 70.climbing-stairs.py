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
        last_option = 1 
        pre_last = 1         
        for i in range(n -1 ):
            tmp = pre_last
            pre_last = pre_last + last_option
            last_option = tmp
        return pre_last            
        
        
        
        
# @lc code=end

