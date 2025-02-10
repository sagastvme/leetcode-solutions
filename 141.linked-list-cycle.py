# @before-stub-for-debug-begin
from python3problem141 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head 
        fast = head.next 
        
        while fast != slow :
            if not fast.next or not fast.next.next :
                return False
            fast = fast.next.next 
            slow = slow.next
        return True 
        
        
# @lc code=end

