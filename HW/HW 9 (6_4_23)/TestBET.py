import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4

        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    def test_evaluate_tree1(self):
        """
                Test a binary tree with 3 operators and 4 operands:
                      *
                     / \
                    +   3
                   / \
                  1   2
                """
        root = BETNode('*')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('3'))
        root.left.add_left(BETNode('1'))
        root.left.add_right(BETNode('2'))
        self.assertEqual(root.evaluate(), 9)
        self.assertEqual(repr(root), '((1+2)*3)')

    def test_evaluate_tree2(self):
        """
               Test a binary tree with 4 operators and 5 operands:
                           -
                          / \
                         /   \
                        +     /
                       / \   / \
                      3   5 6   2
               """
        root = BETNode('-')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('/'))
        root.left.add_left(BETNode('3'))
        root.left.add_right(BETNode('5'))
        root.right.add_left(BETNode('6'))
        root.right.add_right(BETNode('2'))
        self.assertEqual(root.evaluate(), 5)
        self.assertEqual(repr(root), '((3+5)-(6/2))')


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        trees = create_trees(["A", "2", "3", "4"])
        self.assertEqual(len(trees), 7680)

    def test_hand2(self):
        trees = create_trees(["A", "2", "2", "4"])
        self.assertEqual(len(trees), 3840)


class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        trees_repr = find_solutions(["A", "A", "A", "A"])
        self.assertEqual(len(trees_repr), 0)

    def test_A23Q(self):
        trees_repr = find_solutions(["A", "2", "3", "Q"])
        self.assertEqual(len(trees_repr), 33)


unittest.main()
