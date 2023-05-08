import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.nine_hearts = Card('hearts', 9)
        self.ace_clubs = Card('clubs', 1)
        self.four_spades = Card('spades', 4)

    def test_check_for_ace__found(self):
        self.assertEqual(True, CardGame.check_for_ace(self.ace_clubs))

    def test_check_for_ace__not_found(self):
        self.assertEqual(False, CardGame.check_for_ace(self.nine_hearts))

    def test_highest_card(self):
        self.assertEqual(self.nine_hearts, CardGame.highest_card(self.nine_hearts, self.four_spades))

    def test_highest_card__card_order_reversed(self):
        self.assertEqual(self.nine_hearts, CardGame.highest_card(self.four_spades, self.nine_hearts))
    
    def test_cards_total(self):
        cards = [self.nine_hearts, self.four_spades, self.ace_clubs]
        self.assertEqual('You have a total of 14', CardGame.cards_total(cards))