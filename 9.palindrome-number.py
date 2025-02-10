# @before-stub-for-debug-begin
from python3problem9 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        if x < 0 :
            return False
        if x < 10 :
            return True
        
        
        
        dividor = 10 
        
        while x // dividor >9 :
            dividor*= 10 
            
        
        while dividor >= 10 :
            first = self.first_num(x, dividor)
            last = self.last_num(x)
            
            if first != last:
                return False
            
            x = x % dividor
            
            x = x // 10 
            
            dividor = dividor// 100
            
        return True
            
            
                     
                 
        
        
        
        
        
        
    def last_num(self, x ):
        return x % 10 
    def first_num(self, x, dividor):
        return x // dividor
        
        
        
        
        
        
# @lc code=end

