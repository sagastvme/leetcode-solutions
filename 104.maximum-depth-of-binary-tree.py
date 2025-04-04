# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, counter ):
            if not root: 
                return counter 
            counter+=1 
            return max(dfs(root.left, counter ), dfs(root.right, counter ))
            
        if not root:
            return 0
            
        return dfs(root, 0 )
    
    
    # @lc code=end

