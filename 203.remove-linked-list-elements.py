# @before-stub-for-debug-begin
from python3problem203 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head and head.val == val :
            head = head.next
        
        puntero = head 
         
        while head and head.next:
            if head.next.val == val :
                head.next = head.next.next
            else:
                head = head.next
        return puntero
        
# @lc code=end

