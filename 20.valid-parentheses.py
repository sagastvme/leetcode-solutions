#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        translations = {'{': '}', '[': ']', '(': ')'}
        openers_found = []
        
        for symbol in s:
            if symbol in translations:  
                openers_found.append(symbol)
            elif symbol in translations.values(): 
                if len(openers_found) == 0 or symbol != translations[openers_found.pop()]:
                    return False
        
        return len(openers_found) == 0  

               
# @lc code=end

