# @before-stub-for-debug-begin
from python3problem168 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 
            10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 
            18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }

        result = ''

        while columnNumber > 0:
            columnNumber-=1
            remainder = columnNumber % 26
            result += map[remainder + 1]  # Convert remainder to letter
            columnNumber //= 26  # Move to next position
        return result[::-1]

# @lc code=end

