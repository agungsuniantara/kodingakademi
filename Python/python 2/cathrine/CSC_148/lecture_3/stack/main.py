from stack import Stack

# Contoh penggunaan stack
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())

while not stack.is_empty():
    popped_item = stack.pop()
    print("Popped element:", popped_item)

print("Stack size after popping all elements:", stack.size())
