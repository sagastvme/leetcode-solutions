# @before-stub-for-debug-begin
from python3problem169 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0 
        candidate = None 
        
        for num in nums:
            if count == 0 :
                candidate = num 
            if num == candidate:
                count +=1
            else:
                count-=1
        return candidate



# @lc code=end

