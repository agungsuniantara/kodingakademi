class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def traverse_tree(node):
    print(node.value)
    for child in node.children:
        traverse_tree(child)

# Contoh penggunaan
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)

traverse_tree(root)
