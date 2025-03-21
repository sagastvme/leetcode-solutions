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
        return self.find(root)
        
        
    def find(self, p1, counter=0 ):
        if p1:
            counter+= 1 
            left = self.find(p1.left, counter)
            right = self.find(p1.right, counter)
            return left if left > right else right 
        else:
            return counter 
        
# @lc code=end

