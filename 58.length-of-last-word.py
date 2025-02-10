#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = 0

        for index in range(len(s)-1, -1 , -1):
            letter = s[index]
            
            if letter == ' ':
                if last_word != 0:
                    return last_word
            else:
                last_word += 1
        return last_word
        

        
                
            
        
        
        
        
# @lc code=end

