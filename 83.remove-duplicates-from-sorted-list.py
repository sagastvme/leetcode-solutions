# @before-stub-for-debug-begin
from python3problem83 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

    # @lc code=start
# class ListNode:
#         def __init__(self, val=0, next=None):
#             self.val = val
#             self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head 
        
        while pointer:
            if pointer.next and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next                
        return head        
        
# @lc code=end

