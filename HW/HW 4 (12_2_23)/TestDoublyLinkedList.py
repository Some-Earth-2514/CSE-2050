from DoublyLinkedList import DoublyLinkedList as DLL
import unittest


# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        """adds items to front, then removes from front"""
        dll = DLL()
        n = 100

        for j in range(5):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_first(), n - 1 - i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        """adds items to end, then removes from end"""
        dll = DLL()
        n = 100

        for j in range(5):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_last(), n - 1 - i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        """various add/remove patterns"""
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5):  # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i % 2:
                    dll.add_last(i)  # odd numbers - add last
                else:
                    dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n - i)
                if i % 2:
                    self.assertEqual(dll.remove_last(), n - i)  # odd numbers: remove last
                else:
                    self.assertEqual(dll.remove_first(), n - 2 - i)  # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        """Testing __contains__() method"""
        dll = DLL(range(10))
        assert (5 in dll)
        assert not (11 in dll)
        dll.add_first(12)
        assert (12 in dll)
        dll.remove_first()
        assert not (12 in dll)

    def test_neighbors(self):
        """Testing neighbors() method"""
        dll = DLL(range(6))
        assert dll.neighbors(3) == (2, 4)
        assert dll.neighbors(0) == (None, 1)
        assert dll.neighbors(5) == (4, None)

    def test_remove_item(self):
        """Testing remove_nodes() method"""
        dll = DLL([1, 2, 3])
        dll.remove_node(2)
        assert 1 in dll
        assert 2 not in dll
        assert 3 in dll

        try:  # Try to remove a non-existent node
            dll.remove_node(4)
        except RuntimeError:
            pass


unittest.main()
