import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        stack.pop()
        self.assertEqual(stack.peek(), 10)
        stack.pop()
        self.assertIsNone(stack.peek())

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        stack.push(5)
        self.assertFalse(stack.is_empty())

        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

        stack.push(100)
        self.assertEqual(stack.size(), 1)

        stack.push(200)
        self.assertEqual(stack.size(), 2)

        stack.pop()
        self.assertEqual(stack.size(), 1)

        stack.pop()
        self.assertEqual(stack.size(), 0)

if __name__ == '__main__':
    unittest.main()
