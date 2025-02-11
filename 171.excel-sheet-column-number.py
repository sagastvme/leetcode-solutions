# @before-stub-for-debug-begin
from python3problem171 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - 64)
        return result

        
# @lc code=end

