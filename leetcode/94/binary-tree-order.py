# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def extract_list(self, root, lista):
        if not root:
            return

        self.extract_list(root.left, lista)
        lista.append(root.val)
        self.extract_list(root.right, lista)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lista = []
        self.extract_list(root, lista)
        return lista

