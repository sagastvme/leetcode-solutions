#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # The minimum depth of an empty tree is 0

        def helper(node):
            if not node:
                return float('inf')  # Treat None as an infinitely deep path
            
            if not node.left and not node.right:
                return 1  # Leaf node, depth is 1
            
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            
            return min(left_depth, right_depth) + 1

        return helper(root)
# @lc code=end

