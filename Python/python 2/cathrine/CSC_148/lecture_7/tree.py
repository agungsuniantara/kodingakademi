class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Contoh pohon
#            1
#          / | \
#         2  3  4
#        / \     \
#       5   6     7

# Membangun pohon
root = TreeNode(1)
root.add_child(TreeNode(2))
root.add_child(TreeNode(3))
root.add_child(TreeNode(4))
root.children[0].add_child(TreeNode(5))
root.children[0].add_child(TreeNode(6))
root.children[2].add_child(TreeNode(7))
