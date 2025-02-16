# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rec_check(self, elem1: Optional[TreeNode], elem2: Optional[TreeNode]):
        if not elem1 and not elem2:
            return True
        if elem1 and elem2 and elem1.val == elem2.val:
            if self.rec_check(elem1.right, elem2.left) and self.rec_check(elem1.left, elem2.right):
                return True
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.rec_check(root.left, root.right)
