class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_binary_tree(node):
    if node is not None:
        print(node.value)
        traverse_binary_tree(node.left)
        traverse_binary_tree(node.right)

# Contoh penggunaan
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

print("Traversal pada pohon biner:")
traverse_binary_tree(root)
