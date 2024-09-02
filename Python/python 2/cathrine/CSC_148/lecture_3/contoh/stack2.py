class Stack:
  def __init__(self):
    self.item = []
  
  def push(self, a):
    self.item.append(a)
  
  def pop(self):
    return self.item.pop()
  
  def peek(self):
    return self.item[-1]

if __name__ == '__main__':
    objek = Stack()

    objek.push(10)
    objek.push(50)
    objek.push(100)

    print(objek.pop())
    print(objek.peek())
    print(objek.item)
