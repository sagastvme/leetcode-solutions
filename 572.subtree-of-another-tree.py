# @before-stub-for-debug-begin
from python3problem572 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            return root.val == subRoot.val and isSameTree(root.right, subRoot.right) and isSameTree(root.left, subRoot.left)

        def helper(root):
            if not root:
                return False

            if isSameTree(root, subRoot):
                return True

            return helper(root.right) or helper(root.left)

        return helper(root)


# @lc code=end
