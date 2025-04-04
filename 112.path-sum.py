#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, targetSum):
            if root is None:
                return False 
            targetSum -= root.val
            if targetSum == 0 and root.left is None and root.right is None :
                return True 
            return dfs(root.right, targetSum) or dfs(root.left, targetSum)
            
        
        return dfs(root, targetSum)
            
# @lc code=end

