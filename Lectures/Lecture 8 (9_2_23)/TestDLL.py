from DLL import DoublyLinkedList as DLL
import unittest


class TestDLL(unittest.TestCase):
    """test cases for doubly-linked list"""

    def test_addremovefirst(self):
        """add and remove from beginning of dll"""
        n = 0
        dll = DLL()
        for i in range(n):
            self.assertEqual(len(dll), i)
            dll.add_first(i)

        # head---v
        # None <-7<==>6<==>5<==>4<==>3<==>2<==>1<==>0->None
        # tail -----------------------^

        # head---v                 v-----------+
        # None <-7<==6<==5<==4<==3<==2<==1->None     0->None
        # tail --------------------------------^

        # head---v                       v---------+
        # None <-7<==>6<==>5<==>4<==>3<==>2<==>1->None     0->None
        # tail --------------------------^

        for i in range(n):
            self.assertEqual(len(dll), n - i)
            self.assertEqual(dll.remove_last(), i)


unittest.main()
