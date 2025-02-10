# @before-stub-for-debug-begin
from python3problem136 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            res = res ^ num 
        return res 
# @lc code=end

