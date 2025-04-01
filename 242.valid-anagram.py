# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        left = {}
        right = {}
        for i in range(len(t)):
            letterLeft = s[i]
            letterRight = t[i]
            
            if letterLeft in left :
                left[letterLeft]+=1
            else:
                left[letterLeft]=1
                
            if letterRight in right:
                right[letterRight]+=1
            else:
                right[letterRight]=1
                
                 
            
        return right==left 
# @lc code=end

