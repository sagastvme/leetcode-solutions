#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            p1 = root.left 
            p2 = root.right 
            return self.check(p1, p2)
        
    def check(self, p1, p2):
        if not p1 and not p2 :
            return True 
        elif not p1 or not p2:
            return False 
        if p1.val != p2.val :
            return False 
        return self.check( p1.left, p2.right  ) and self.check(p1.right , p2.left)
# @lc code=end

