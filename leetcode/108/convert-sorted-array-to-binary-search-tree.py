# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def print(self, tree: TreeNode | None) -> None:
        if not tree:
            return

        self.print(tree.left)
        print(tree.val)
        self.print(tree.right)

    def createTree(self, nums, tree) -> TreeNode | None:
        if not nums:
            return None
        tree.val = nums[len(nums) // 2]
        print(tree.val)
        tree.right = self.createTree(nums[len(nums) // 2 + 1: len(nums)], TreeNode())
        tree.left = self.createTree(nums[0 : len(nums) // 2], TreeNode())
        return tree

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.createTree(nums, TreeNode())


abc = Solution().sortedArrayToBST([1,2,3,4,5])
Solution().print(abc)
