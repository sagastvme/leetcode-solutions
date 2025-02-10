# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x 
        
        
        while left<= right:
            
            middle = (left + right) // 2 
            num = middle ** 2 
            
            if num == x :
                return middle 
            elif num > x :
                right = middle -1 
            elif num < x :
                left = middle + 1 
        return left -1 
            
            
        
        
        
        
# @lc code=end

