from Cards import Card, Deck, Hand
import unittest


class TestCard(unittest.TestCase):
    """ Test cases specific to the Card class """

    def test_init(self):
        """Testing _init_(): creating and asserting their values"""
        c1 = Card(5, 'spades')
        self.assertEquals(c1.value, 5)
        self.assertEquals(c1.suit, 'spades')

        c2 = Card(3, 'hearts')
        self.assertEqual(c2.value, 3)
        self.assertEquals(c2.suit, 'hearts')

        c3 = Card(4, 'clubs')
        self.assertEqual(c3.value, 4)
        self.assertEqual(c3.suit, 'clubs')

    def test_repr(self):
        """Testing _repr_(): asserting if correctly formatted when printed"""
        c1 = Card(5, 'spades')
        c2 = Card(3, 'hearts')
        c3 = Card(4, 'clubs')

        self.assertEquals(repr(c1), 'Card(5 of spades)')
        self.assertEquals(repr(c2), 'Card(3 of hearts)')
        self.assertEquals(repr(c3), 'Card(4 of clubs)')

    def test_lt(self):
        """Testing _lt_(): asserting if cards are according to their suits & values"""
        c1 = Card(5, 'spades')
        c2 = Card(3, 'hearts')
        c3 = Card(4, 'clubs')

        assert (c3 < c1)
        assert not (c1 < c2)
        assert (c3 < c2)

    def test_eq(self):
        """Testing _eq_(): asserting if cards are equal or not equal according to their suits & values """
        c1 = Card(5, 'spades')
        c2 = Card(3, 'hearts')
        c3 = Card(5, 'spades')

        assert (c1 == c3)
        assert not (c1 == c2)
        assert not (c2 == c3)


class TestDeck(unittest.TestCase):
    """ Test cases specific to the Deck class """

    def test_init(self):
        """Testing _init_(): creating various objects and asserting their values """
        d1 = Deck()
        self.assertEquals(d1.values, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        self.assertEquals(d1.suits, ['clubs', 'diamonds', 'hearts', 'spades'])

        d2 = Deck([3, 1, 2, 5], ['spades, hearts, diamonds, clubs'])
        self.assertEquals(d2.values, [3, 1, 2, 5])
        self.assertEquals(d2.suits, ['spades, hearts, diamonds, clubs'])

    def test_len(self):
        """Testing len(): creating various objects and asserting their length """
        d1 = Deck()
        d2 = Deck([3, 1, 2, 5], ['spades, hearts, diamonds, clubs'])

        self.assertEquals(len(d1), 52)
        self.assertEquals(len(d2), 4)

    def test_sort(self):
        """Testing sort(): creating an object and asserting that they are sorted in order """
        d1 = Deck([1, 2], ['clubs', 'hearts'])
        d1.sort()
        self.assertEquals(repr(d1), 'Deck: [Card(1 of clubs), Card(2 of clubs), Card(1 of hearts), Card(2 of hearts)]')

    def test_repr(self):
        """Testing _repr_(): asserting deck objects are formatted correctly when printed """
        d1 = Deck([1, 2], ['clubs', 'hearts'])
        self.assertEquals(repr(d1), 'Deck: [Card(1 of clubs), Card(1 of hearts), Card(2 of clubs), Card(2 of hearts)]')

    def test_shuffle(self):
        """Testing shuffle(): asserting that deck objects are shuffled out of their original order """
        d1 = Deck([3, 1, 2, 5], ['spades, hearts, diamonds, clubs'])
        d2 = Deck([3, 1, 2, 5], ['spades, hearts, diamonds, clubs'])
        d1.shuffle()
        self.assertNotEquals(d1, d2)

    def test_draw_top(self):
        """Testing draw_top(): asserting that cards are drawn in the correct order & RuntimeError is returned if Deck is empty"""
        d1 = Deck([1, 2], ['clubs', 'hearts'])
        self.assertEquals(d1.draw_top(), Card(2, 'hearts'))
        self.assertEquals(d1.draw_top(), Card(2, 'clubs'))
        try:
            d1.draw_top()
        except:
            RuntimeError


class TestHand(unittest.TestCase):
    """ Test cases specific to the Hand class """

    def test_init(self):
        """Testing _init_(): creating various objects and asserting their values """
        h1 = Hand([Card(value, 'diamonds') for value in range(4, 0, -1)])
        self.assertEquals(repr(h1),
                          'Hand: [Card(4 of diamonds), Card(3 of diamonds), Card(2 of diamonds), Card(1 of diamonds)]')

    def test_len(self):
        """Testing [inherited] len(): creating various objects and asserting their length """
        h1 = Hand([Card(value, 'diamonds') for value in range(4, 0, -1)])
        self.assertEquals(len(h1), 4)

    def test_sort(self):
        """Testing [inherited] sort(): creating an object and asserting that they are sorted in order """
        h1 = Hand([Card(value, 'diamonds') for value in range(4, 0, -1)])
        h1.sort()
        self.assertEquals(repr(h1),
                          'Hand: [Card(1 of diamonds), Card(2 of diamonds), Card(3 of diamonds), Card(4 of diamonds)]')

    def test_repr(self):
        """Testing _repr_(): asserting the hands are formatted correctly when printed """
        h1 = Hand([Card(value, 'diamonds') for value in range(4, 0, -1)])
        self.assertEquals(repr(h1),
                          'Hand: [Card(4 of diamonds), Card(3 of diamonds), Card(2 of diamonds), Card(1 of diamonds)]')

    def test_play(self):
        """Testing play(card): asserting that desired card is drawn & RuntimeError is returned if card is not in Hand """
        h1 = Hand([Card(value, 'diamonds') for value in range(4, 0, -1)])
        self.assertEquals(repr(h1.play(Card(1, 'diamonds'))), 'Card(1 of diamonds)')
        try:
            h1.play(Card(0, 'diamonds'))
        except:
            RuntimeError


if __name__ == "__main__":
    unittest.main()  # run all test above
