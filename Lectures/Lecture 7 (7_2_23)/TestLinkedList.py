from LinkedList import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    """LinkedList tests"""

    def test_addfirst_removefirst(self):
        n = 5
        ll = LinkedList()

        for i in range(n):
            self.assertEqual(len(ll), i)
            ll.add_first(i)

        # head 4, 3, 2, 1, 0 -> None
        # tail ------------^

        for i in range(n):
            self.assertEqual(len(ll), n - 1)
            self.assertEqual(ll.remove_first(), n - 1 - i)


unittest.main()
