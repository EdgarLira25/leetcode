class Solution:
    def extract_list(self, root, lista):
        if not root:
            return

        lista.append(root.val)
        self.extract_list(root.left, lista)
        self.extract_list(root.right, lista)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lista = []
        self.extract_list(root, lista)
        return lista
