class Solution:
    def extract_list(self, root, lista):
        if not root:
            return

        self.extract_list(root.left, lista)
        self.extract_list(root.right, lista)
        lista.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lista = []
        self.extract_list(root, lista)
        return lista
