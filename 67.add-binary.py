# @before-stub-for-debug-begin
from python3problem67 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a)
        if len(b)> max_len:
            max_len = len(b)
            
        if max_len > len(b):
            for i in range(  (max_len- len(b)) ):
                b = "0" + b 
        if max_len > len(a):
            for i in range( (max_len- len(a))   ):
                a = "0" + a 
        
        carry = 0
        sum = "" 
        for i in range(len(a)-1, -1, -1 ):
            
            num_a = int(a[i])
            num_b =int(b[i])
            res = num_a + num_b + carry 
             
            sum = str( res % 2   ) + sum
            carry = res // 2
        print(sum)
        
        if carry == 1 :
            return "1" + sum 
        return sum 
            
            
            
            
            
        
        
                   
            
        
        
        
            
             
            
# @lc code=end

