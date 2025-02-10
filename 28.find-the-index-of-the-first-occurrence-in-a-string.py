# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0 

        needle_len = len(needle)
        hay_len = len(haystack)

        loop_limit = hay_len - needle_len + 1

        for i in range(loop_limit):
            matched = True
            for j in range(needle_len) :
                if haystack[i + j] != needle[j] and matched:
                    matched = False
                    break
            if matched:
                return i 
        return -1

        
        
        
# @lc code=end

