# @before-stub-for-debug-begin
from python3problem145 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res =[]
        visited = []
        while root or stack :
            if root:
                if root in visited:
                    res.append(root.val) 
                    root = None
                else:
                    stack.append(root)
                    stack.append(root.right)
                    visited.append(root)
                    root = root.left
            else:
                root = stack.pop()
        return res     
            
            
# @lc code=end

