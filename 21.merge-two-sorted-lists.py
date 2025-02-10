# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        pointer = dummy 
        
        
        while list1 and list2:
            if list1.val > list2.val :
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            pointer = pointer.next            
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
            
        return dummy.next
            
        
        
        
        
        
# @lc code=end

