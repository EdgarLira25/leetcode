from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def aux_depth(self, root: Optional[TreeNode], depth: int, max: int) -> int:
        if not root:
            return max

        depth += 1
        if depth > max:
            max = depth

        if root.left:
            depth_left = self.aux_depth(root.left, depth, max)
            if depth_left > max:
                max = depth_left
        if root.right:
            depth_right = self.aux_depth(root.right, depth, max)
            if depth_right > max:
                max = depth_right

        print(depth, max)
        return max

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.aux_depth(root, 0, 0)


print(Solution().maxDepth(TreeNode(left=TreeNode())))
