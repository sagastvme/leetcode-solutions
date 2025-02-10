#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {'I': 1, 'V': 5, 'X': 10 , 'L': 50 , 'C': 100, 'D': 500, 'M':1000  }
        count = 0 
        
        for index, char in enumerate(s) :
            translation = translations[char]
            
            if index + 1  == len(s):
                count+= translation
            elif translation < translations[s[index+1]]:
                count -= translation
            else:
                count += translation
        return count 
            
        
        
        
         
# @lc code=end

