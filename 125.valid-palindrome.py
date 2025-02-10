#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1 
        s = s.lower()
        while l< r :
            
            while l < r and  s[l].isalnum() is not True : 
                l +=1 
            while r > l and s[r].isalnum() is not True:
                r -= 1 
                         
            if s[l] != s[r]:
                return False
            l +=1 
            r-=1 
        return True 
            
            
            
        
# @lc code=end

