# @before-stub-for-debug-begin
from python3problem191 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         counter = 0 
#         while n > 0 :
#             bit = n % 2 
#             if bit != 0 :
#                 counter+=1
#             n = n //2 
#         return counter
class Solution:
        def hammingWeight(self, n: int) -> int:
            count = 0
            while n:
                n = n & n - 1  
                count += 1
            return count

# @lc code=end

