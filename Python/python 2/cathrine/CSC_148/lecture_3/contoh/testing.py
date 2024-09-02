import unittest
from stack2 import Stack

class TestStack(unittest.TestCase):
    def test_pop(self):
        angka = Stack()
        angka.push(10)
        angka.push(50)
        
        last = angka.item[-1]
        self.assertEqual(angka.pop(), last)

if __name__ == '__main__':
    unittest.main()

