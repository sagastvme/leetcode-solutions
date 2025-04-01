# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

class Solution:
    def isPalindrome(self, s: str) -> bool:
      sanitized = []
      for char in s :
          if char.isalnum():
              sanitized.append(char.lower())
      
      
      if not sanitized:
          return True 
      
      print(sanitized)
      
      end = len(sanitized) -1 
      start = 0 
      
      
      while start < end:
          if sanitized[start] != sanitized[end]:
              return False 
          start+=1 
          end-=1 
      return True 
          
          
            
            
        
# @lc code=end

