# @before-stub-for-debug-begin
from python3problem100 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q )
    def check(self ,p,q):
        if not p and not q :
            return True 
        elif not p or not q :
            return False 
        if p.val != q.val :
            return False 
        return self.check(p.left,q.left) and self.check(q.right, p.right)
# @lc code=end

