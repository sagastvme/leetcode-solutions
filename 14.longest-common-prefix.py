# @before-stub-for-debug-begin
from python3problem14 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest_word = strs[0]
        for index, str in enumerate(strs):
            if len(str) < len(smallest_word):
                smallest_word = str

        for index, letter in enumerate( smallest_word):
            
            for word in strs:
                if letter!= word[index]:
                    return smallest_word[:index]
            
        return smallest_word
            
        
        
        
        
        
# @lc code=end

