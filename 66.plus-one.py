# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_represented = 0 
        multiplier = 10 ** (len(digits)-1)

        for i in range(len(digits)):
            num_represented += digits[i] * multiplier
            multiplier = multiplier//10
        
        num_represented += 1 
        
        multiplier = 10 ** (len(digits)-1)
        
        final_arr = []
        while multiplier> 0 :
            last_digit = num_represented//multiplier
            
            if last_digit == 10 :
                final_arr.append(1)
                final_arr.append(0)
            else:
                final_arr.append(last_digit)
            num_represented = num_represented % multiplier 
            multiplier //= 10 
        return final_arr
                    
        
        
        
        
        
# @lc code=end

