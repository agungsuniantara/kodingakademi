class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return data
        else:
            return None

    def is_empty(self):
        return self.front is None

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            return None

# Contoh penggunaan linked list queue
ll_queue = LinkedListQueue()
ll_queue.enqueue(1)
ll_queue.enqueue(2)
ll_queue.enqueue(3)

print("Front Element:", ll_queue.peek())

ll_queue.dequeue()
ll_queue.dequeue()

print("Front Element after dequeue:", ll_queue.peek())
