# @before-stub-for-debug-begin
from python3problem160 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        startA = headA
        startB = headB
        
        while headA != headB:
            if headA is None:
                headA = startB
            else:
                headA = headA.next
            
            if headB is None:
                headB = startA
            else:
                headB = headB.next
              
        return headA
            
            
            
            
            
            
        
# @lc code=end

