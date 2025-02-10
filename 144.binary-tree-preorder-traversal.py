# @before-stub-for-debug-begin
from python3problem144 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(root):
            if root is None:
                return 
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result
# @lc code=end

