class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
        else:
            return None

# Contoh penggunaan linked list stack
ll_stack = LinkedListStack()
ll_stack.push(1)
ll_stack.push(2)
ll_stack.push(3)

print("Top Element:", ll_stack.top.data if ll_stack.top else None)

ll_stack.pop()
ll_stack.pop()

print("Top Element:", ll_stack.top.data if ll_stack.top else None)
