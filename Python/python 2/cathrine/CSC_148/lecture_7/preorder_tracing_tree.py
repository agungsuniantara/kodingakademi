class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def preorder_traversal(node):
    if node is None:
        return
    
    print(node.data, end=" ")  # Visit the current node
    
    for child in node.children:
        preorder_traversal(child)  # Recursive call for each child

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

# Preorder traversal pada pohon
print("Preorder Traversal:")
preorder_traversal(root)
