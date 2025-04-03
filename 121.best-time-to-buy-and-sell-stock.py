# @before-stub-for-debug-begin
from python3problem121 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        left = 0 
        right = 1
        
        while right < len(prices) :
            
            if prices[left] > prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                
                if diff > maxDiff:
                    maxDiff = diff 
                
            right += 1 
                
        return maxDiff
                        
            
            
            
# @lc code=end

