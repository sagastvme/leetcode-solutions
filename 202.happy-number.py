# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            res = 0 
            while n > 0  :
                    lastDigit = n % 10
                    n = n // 10 
                    res+= lastDigit**2                
            n = res 
        return n == 1 
        
# @lc code=end

