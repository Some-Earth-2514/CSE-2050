from Stack import Stack, Queue
import unittest


class TestStack(unittest.TestCase):
    """unittest for Stack"""

    def test_pushpop(self):
        s = Stack()
        n = 10

        for i in range(n):
            s.push(i)

        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 <- top of the stack

        for i in range(n):
            self.assertEqual(s.pop(), n - 1 - i)

    def test_queue(self):
        q = Queue()
        n = 10

        for i in range(n):
            q.enqueue(i)

        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 <- top of the stack

        for i in range(n):
            self.assertEqual(q.dequeue(), n - 1 - i)


unittest.main()
