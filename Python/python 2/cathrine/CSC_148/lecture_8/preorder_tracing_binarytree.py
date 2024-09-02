class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")  # Visit the current node
        preorder_traversal(node.left)  # Traverse left subtree recursively
        preorder_traversal(node.right)  # Traverse right subtree recursively

# Contoh pohon biner
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7

# Membuat simpul-simpul untuk pohon biner
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Preorder Traversal:")
preorder_traversal(root)
