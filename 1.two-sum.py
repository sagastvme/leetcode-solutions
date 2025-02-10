# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums) :
            missing_num = target - num 
            if missing_num in map :
                return [map[missing_num], index]
            else :
                map[num]  = index
                 
            
        
# @lc code=end

