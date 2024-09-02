class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Membuat simpul pertama
node1 = Node(1)

# Membuat simpul kedua
node2 = Node(2)

# Membuat simpul ketiga
node3 = Node(3)

# Menyambungkan simpul pertama ke simpul kedua
node1.next = node2

# Menyambungkan simpul kedua ke simpul ketiga
node2.next = node3

# Menampilkan data dari setiap simpul dalam linked list
print("Data pada simpul pertama:", node1.data)
print("Data pada simpul kedua:", node1.next.data)
print("Data pada simpul ketiga:", node1.next.next.data)

# Menampilkan data menggunakan perulangan
current_node = node1

while current_node:
    print("Data:", current_node.data)
    current_node = current_node.next
