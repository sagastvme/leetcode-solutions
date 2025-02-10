# @before-stub-for-debug-begin
from python3problem118 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows ):
            rowArr = []
            previousRow = row - 1 > 0
            for number in range(row + 1 ):
                if previousRow: 
                    if number == 0 or number == row:
                        rowArr.append(1)
                    else:
                        num1 = result[row - 1 ][number - 1 ]
                        num2 = result[row - 1][number]
                        rowArr.append(num1 + num2)                     
                else:
                    rowArr.append(1)
            result.append(rowArr)
        return result
                
# @lc code=end

