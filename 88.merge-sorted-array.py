# @before-stub-for-debug-begin
from python3problem88 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted nums1ay
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_pointer = m + n -1 
        first_pointer = m -1
        second_pointer = n -1
         
        while first_pointer >=  0 and second_pointer >= 0 :
            if nums1[first_pointer] > nums2[second_pointer] : 
                nums1[final_pointer] = nums1[first_pointer]
                first_pointer -= 1 
            else:
                nums1[final_pointer] = nums2[second_pointer]
                second_pointer -=1 
            final_pointer -= 1
        if second_pointer >= 0 :
            for i in range(second_pointer + 1):
                nums1[i] = nums2[i]       
            
# @lc code=end

