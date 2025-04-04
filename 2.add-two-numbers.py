# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def unpack(list ):
            res = [] 
            total = 0 
            counter = 1
            while list :
                res.append(list.val)
                list = list.next
            for i in range(len(res)):
                base = 1 * counter
                num = res[i] * base 
                total += num 
                counter *= 10 
            return total 
        left = unpack(l1)
        right = unpack(l2)
        result = left + right
        
        result_to_array = []
        
        while result > 0 :
            last = result % 10
            result_to_array.append(last)
            result = result // 10
        if not result_to_array:
            result_to_array = [0]
        print('result to array thta im working with ' , result_to_array)
        linked_list = ListNode()
        head_reference = linked_list
        for i in result_to_array:
            node = ListNode()
            node.val = i 
             
            linked_list.next = node 
            linked_list = linked_list.next
            
        return head_reference.next
        
# @lc code=end

