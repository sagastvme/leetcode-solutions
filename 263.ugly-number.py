# @before-stub-for-debug-begin
from python3problem263 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        list = [2,3,5]
        correct = True
        while n > 1 and correct:
            used = False
            for i in list :
                if n >= i and n % i == 0 :
                    n = n // i
                    used = True
                    break
            if used == False:
                return False
        return n == 1
        
# @lc code=end

