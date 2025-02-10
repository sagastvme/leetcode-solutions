#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            
            # If a subtree is unbalanced, propagate -1 up the call stack
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        # The tree is balanced if height does not return -1
        return height(root) != -1

# @lc code=end

