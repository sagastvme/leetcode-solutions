#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        streak = 0 
        for num in myset :
            number_before = num - 1 
            if number_before not in myset:
                new_streak = 0
                while (num + new_streak) in myset:
                    new_streak+= 1 
                streak = max(streak, new_streak)
        return streak
        
        

# @lc code=end

