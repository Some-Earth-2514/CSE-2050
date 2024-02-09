import itertools


class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                     '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None:
            return False
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))

    # START HERE
    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def evaluate(self):
        if self.value in self.OPERATORS:
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            if self.value == "+":
                return left_val + right_val
            elif self.value == "-":
                return left_val - right_val
            elif self.value == "*":
                return left_val * right_val
            elif self.value == "/":
                if right_val == 0:
                    return float('nan')
                return left_val / right_val
        else:
            return self.CARD_VAL_DICT.get(self.value)

    def __repr__(self):
        if self.value in self.OPERATORS:
            return f"({repr(self.left)} + {str(self.value)} + {repr(self.right)})"
        else:
            return str(self.value)


def create_expression_tree(expression):
    stack = []
    for i in expression:
        if i in BETNode.OPERATORS:
            right = stack.pop()
            left = stack.pop()
            node = BETNode(i, left, right)
            stack.append(node)
        else:
            node = BETNode(i)
            stack.append(node)
    return stack.pop()


def create_trees(cards):
    trees = set()

    for shape in ['CCXCCXX', 'CCXCXCX', 'CCCXXCX', 'CCCXCXX', 'CCCCXXX']:
        for cards_perm in itertools.permutations(cards):
            for op_perm in itertools.product(BETNode.OPERATORS, repeat=3):
                expression = ''
                op_idx = 0
                cards_id = 0
                for c in shape:
                    if c == 'C':
                        expression += cards_perm[cards_id]
                        cards_id += 1
                    else:
                        expression += op_perm[op_idx]
                        op_idx += 1
                tree = create_expression_tree(expression)
                trees.add(tree)
    return trees


def find_solutions(cards):
    trees_24 = set()
    trees = create_trees(cards)
    for tree in trees:
        if tree.evaluate() == 24:
            trees_24.add(repr(tree))
    return trees_24
