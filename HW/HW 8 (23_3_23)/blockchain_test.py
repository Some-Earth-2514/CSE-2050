import unittest
from hashmap import HashMap as hm
from blockchain import Transaction, Block, Ledger, Blockchain


class Test_Hash_Map(unittest.TestCase):
    """
    Class that tests HashMap ADT which is a wrapper of the
    Python dictionary
    """
    def test_contains(self):
        """
        Creates an instance of Hashmap ADT and checks if item in map
        """
        dict0 = hm()
        self.assertFalse(0 in dict0)
        dict0["Sand"] = 500
        self.assertTrue("Sand" in dict0)
        dict0.remove("Sand")
        self.assertFalse("Sand" in dict0)

        dict1 = hm()
        dict1["A"] = 700
        dict1["B"] = 350
        dict1["C"] = 700
        dict1.remove("C")

        self.assertTrue("A" in dict1)
        self.assertTrue("B" in dict1)
        self.assertFalse("C" in dict1)

    def test_changing_value(self):
        """
        Creates an instance of Hashmap ADT and checks if a value gets updated
        """
        dict0 = hm()
        dict0["Eat"] = 100
        self.assertEqual(dict0["Eat"], 100)
        dict0["Eat"] = 275
        self.assertEqual(dict0["Eat"], 275)

        dict1 = hm()
        dict1["Ball"] = 27
        self.assertEqual(dict1["Ball"], 27)
        dict1["Ball"] = 347
        self.assertEqual(dict1["Ball"], 347)


class Test_Transaction(unittest.TestCase):
    """
    Class that tests Transaction class that holds the sender user, receiver user
    and the amount of HuskyCoin sent
    """
    def test_transaction(self):
        """
        Creates an instance of Transaction and tests that passed elements are correct
        """
        trans1 = Transaction("Eat", "Sand", 100)
        self.assertEqual(trans1.from_user, "Eat")
        self.assertEqual(trans1.to_user, "Sand")
        self.assertEqual(trans1.amount, 100)
        self.assertEqual(repr(trans1), "(Sender: Eat, Receiver: Sand, Amount: 100 HuskyCoin)")

        trans2 = Transaction("John", "Cena", 500)
        self.assertEqual(trans2.from_user, "John")
        self.assertEqual(trans2.to_user, "Cena")
        self.assertEqual(trans2.amount, 500)
        self.assertEqual(repr(trans2), "(Sender: John, Receiver: Cena, Amount: 500 HuskyCoin)")


class Test_Block(unittest.TestCase):
    """
    Class that test the Block class that holds a list of transactions
    """
    def test_adding_transaction(self):
        """
        Creates an instance of block and keeps adding,
        checking that it's added to the list of transactions
        """
        block1 = Block()
        trans1 = ("Mango", "Sand", 720)
        block1.add_transaction(trans1)

        self.assertIn(trans1, block1.transactions)
        trans2 = ("Nickel", "Max", 800)
        block1.add_transaction(trans2)

        self.assertIn(trans2, block1.transactions)
        trans3 = ("Philip", "Hailey", 200)
        block1.add_transaction(trans3)

        self.assertIn(trans3, block1.transactions)

    def test_string_of_trans(self):
        """
        Creates an instance of block and adds transactions.
        Checks string representation of block
        """
        block1 = Block()
        trans1 = ("Clark", "Kent", 50)

        block1.add_transaction(trans1)
        trans2 = ("Ann", "Won", 136)

        block1.add_transaction(trans2)
        trans3 = ("Summer", "Winter", 853)

        block1.add_transaction(trans3)
        self.assertEqual(repr(block1),
                         "Transactions: [('Clark', 'Kent', 50), ('Ann', 'Won', 136), ('Summer', 'Winter', 853)]")


class Test_Ledger(unittest.TestCase):
    """
    Class that tests the Ledger class that checks if sufficient funds,
    allows deposits, and allows transfers
    """
    def test_has_funds(self):
        """
        Creates an instance of Ledger and tests if a user has funds
        """
        ledger1 = Ledger()
        try:
            ledger1.has_funds("Sand", 100)
        except:
            "Sand is not in Ledger"

        ledger1._hashmap["Sand"] = 100
        self.assertTrue(ledger1.has_funds("Sand", 100))

        ledger1._hashmap["Squid"] = 57
        self.assertFalse(ledger1.has_funds("Squid", 100))

        ledger1._hashmap["Rachel"] = 540
        self.assertFalse(ledger1.has_funds("Rachel", 1000))

    def test_deposit(self):
        """
        Creates an instance of Ledger and tests the deposit method
        """
        ledger1 = Ledger()
        try:
            ledger1.deposit("Timmy", 729)
        except:
            "Timmy is not in Ledger"

        ledger1._hashmap["Timmy"] = 0
        ledger1.deposit("Timmy", 476)
        self.assertEqual(ledger1._hashmap["Timmy"], 476)

        ledger1._hashmap["Evan"] = 0
        ledger1.deposit("Evan", 562)
        self.assertEqual(ledger1._hashmap["Evan"], 562)

    def test_transfer(self):
        """
        Creates an instance of Ledger and tests the transfer method
        """
        ledger1 = Ledger()
        try:
            ledger1.transfer("Felix", 20)
        except:
            "Felix is not in Ledger"

        ledger1._hashmap["Felix"] = 350
        ledger1.transfer("Felix", 20)
        self.assertEqual(ledger1._hashmap["Felix"], 330)

        ledger1._hashmap["John"] = 182
        ledger1.transfer("John", 149)
        self.assertEqual(ledger1._hashmap["John"], 33)

    def test_repr(self):
        """
        Uses previous tests, transfer and deposit, to write a ledger
        """
        ledger1 = Ledger()

        ledger1._hashmap["Tim"] = 0
        ledger1.deposit("Tim", 476)
        self.assertEqual(ledger1._hashmap["Tim"], 476)

        ledger1._hashmap["Evan"] = 0
        ledger1.deposit("Evan", 562)
        self.assertEqual(ledger1._hashmap["Evan"], 562)

        ledger1._hashmap["Felix"] = 350
        ledger1.transfer("Felix", 20)
        self.assertEqual(ledger1._hashmap["Felix"], 330)

        ledger1._hashmap["John"] = 182
        ledger1.transfer("John", 149)
        self.assertEqual(ledger1._hashmap["John"], 33)

        self.assertEqual(repr(ledger1), "Ledger: {'Tim': 476, 'Evan': 562, 'Felix': 330, 'John': 33}")


class Test_Blockchain(unittest.TestCase):
    """
    Class that tests the Blockchain class that has an add block method,
    validate chain method, and a root block
    """
    def test_add_block(self):
        """
        Creates an instance of Blockchain and block along with a starter block
        """
        bc1 = Blockchain()
        block1 = Block()
        trans1 = Transaction("Mike", "Ann", 200)
        trans2 = Transaction("Mike", "Ann", 50)
        trans3 = Transaction("A", "Jill", 500)

        bc1.distribute_mining_reward("Mike")
        bc1.distribute_mining_reward("Ann")
        bc1.distribute_mining_reward("A")

        block1.add_transaction(trans1)
        block1.add_transaction(trans2)
        block1.add_transaction(trans3)

        bc1.add_block(block1)
        self.assertEqual(repr(bc1._bc_ledger),
                         "Ledger: {'ROOT': 996999, 'Mike': 750, 'Ann': 1250, 'A': 500, 'Jill': 500}")
        self.assertTrue(bc1.add_block(block1))
        trans4 = Transaction("Mike", "Ann", 5000)
        block1.add_transaction(trans4)
        try:
            bc1.add_block(block1)
        except:
            "Mike does not have enough funds to send 5000 to Ann"

    def test_validate_chain(self):
        """
        Creates an instance of blockchain and multiple blocks to validate the block chain
        """
        bc1 = Blockchain()
        block1 = Block()
        block2 = Block()
        block3 = Block()

        trans1 = Transaction("Mike", "Ann", 200)
        trans2 = Transaction("Mike", "Ann", 50)
        trans3 = Transaction("A", "Jill", 500)
        trans4 = Transaction("Sand", "Astrid", 63)
        trans5 = Transaction("Milo", "Reed", 128)

        bc1.distribute_mining_reward("Mike")
        bc1.distribute_mining_reward("Ann")
        bc1.distribute_mining_reward("A")
        bc1.distribute_mining_reward("Sand")
        bc1.distribute_mining_reward("Milo")

        block1.add_transaction(trans1)
        block1.add_transaction(trans2)
        block2.add_transaction(trans3)
        block2.add_transaction(trans4)
        block3.add_transaction(trans5)

        bc1.add_block(block1)
        bc1.add_block(block2)
        bc1.add_block(block3)

        self.assertEqual(bc1.validate_chain(), [])

        tamper_transaction = Transaction("Mike", "Ann", 100)
        block1.add_transaction(tamper_transaction)
        self.assertEqual(bc1.validate_chain(), [
            "[(Sender: Mike, Reciever: Ann, Amount: 200 HuskyCoin), (Sender: Mike, Reciever: Ann, Amount: 50 "
            "HuskyCoin), (Sender: Mike, Reciever: Ann, Amount: 100 HuskyCoin)]"])


unittest.main()
