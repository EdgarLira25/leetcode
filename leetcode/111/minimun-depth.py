# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def aux_depth(self, root: Optional[TreeNode], depth: int, min: float) -> float:
        if not root:
            return min

        depth += 1

        if not root.left and not root.right:
            if depth < min:
                return depth

        min_left = self.aux_depth(root.left, depth, min)
        if min_left < min:
            min = min_left
        min_right = self.aux_depth(root.right, depth, min)
        if min_right < min:
            min = min_right

        return min

    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = self.aux_depth(root, 0, float("inf"))
        return int(result) if result != float("inf") else 0


a = TreeNode(
    right=TreeNode(
        right=TreeNode(right=TreeNode(right=TreeNode(right=TreeNode(val=4))))
    )
)
print(Solution().minDepth(a))
