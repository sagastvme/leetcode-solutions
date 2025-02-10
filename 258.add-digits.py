# @before-stub-for-debug-begin
from python3problem258 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        def add_digits(num):
            total = 0 
            while num > 0 :
                total += num % 10 
                num = num // 10 
            return total     
        
        while num >= 10 :
            num = add_digits(num)            
        return num 
        
            
# @lc code=end

