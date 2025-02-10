# @before-stub-for-debug-begin
from python3problem119 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):
            num_anterior = result[i-1]
            por_averiguar = (rowIndex+1) - i  
            resueltos =  i 
            result[i] = (num_anterior * por_averiguar)//resueltos
        return result
# @lc code=end

