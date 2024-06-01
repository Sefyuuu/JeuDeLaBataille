import random
from collections import Counter

# Define a Card class
class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

# Define a Deck class
class Deck:
    def __init__(self,condition):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        
        # Create deck based on condition
        self.deckcondition = []
        for key, value in condition.items():
            for i in range(value):
                self.deckcondition.append(Card(Card.suits[i % 4], key))  # Use modulo to avoid index error
                print(key)

        # Calculate the number of remaining cards needed
        carte_restante = 16 - len(self.deckcondition)
        print(f"Cards remaining to complete deck: {carte_restante}")

        # Remove cards that match the condition from the full deck
        for card2 in self.deckcondition:
            for card1 in self.cards:
                if card2.suit == card1.suit and card2.rank == card1.rank:
                    self.cards.remove(card1)
                    break  # Break to avoid removing multiple cards

        print(f"Remaining cards in full deck after removal: {len(self.cards)}")

        # If needed, complete the deck with random cards
        if carte_restante > 0:
            deckshuffle = self.deckcondition + self.cards[:carte_restante]
        else:
            deckshuffle = self.deckcondition

        random.shuffle(deckshuffle)
        self.deck1 = deckshuffle
        self.deck2 = self.cards[carte_restante:]
        
        print(f"Deck 1: {self.deck1}")
        print(f"Deck 2: {self.deck2}")
# Define a Player class
class Player:
    def __init__(self, name):
        self.name = name

# Define the Game class
class WarGame:
    def __init__(self, player1, player2,condition):
        self.player1 = player1
        self.player2 = player2
        self.condition = condition
        self.deck = Deck(self.condition)
        self.player1_deck = self.deck.deck1
        self.player2_deck = self.deck.deck2

    def simulate_game(self):
        count = 0
        carte = []
        while self.player1_deck and self.player2_deck and count < 5000:
            p1_card = self.player1_deck.pop(0)
            p2_card = self.player2_deck.pop(0)
            carte = [p1_card,p2_card]
            if Card.ranks.index(p1_card.rank) > Card.ranks.index(p2_card.rank):
                random.shuffle(carte)
                self.player1_deck.extend(carte)
                carte = []
            elif Card.ranks.index(p2_card.rank) > Card.ranks.index(p1_card.rank):
                random.shuffle(carte)
                self.player2_deck.extend(carte)
                carte = []
            else:
                if len(self.player1_deck) < 2:
                    return self.player2.name
                elif len(self.player2_deck) < 2:
                    return self.player1.name
                else:
                    winner = self.handle_war(carte)
                    if winner:
                        return winner
            count  = count + 1

        if not self.player1_deck:
            return self.player2.name
        elif not self.player2_deck:
            return self.player1.name
        else:
            return 'Draw'
            
    def handle_war(self,carte):
        if len(self.player1_deck) < 2:
            return self.player2.name
        elif len(self.player2_deck) < 2:
            return self.player1.name
        p1_hidden_card =  self.player1_deck.pop(0)
        p2_hidden_card = self.player2_deck.pop(0)
        p1_card = self.player1_deck.pop(0)
        p2_card = self.player2_deck.pop(0)
        carte.extend([p1_card,p2_card,p1_hidden_card,p2_hidden_card])
        if Card.ranks.index(p1_card.rank) > Card.ranks.index(p2_card.rank):
            random.shuffle(carte)
            self.player1_deck.extend(carte)
            carte = []
        elif Card.ranks.index(p2_card.rank) > Card.ranks.index(p1_card.rank):
            random.shuffle(carte)
            self.player2_deck.extend(carte)
            carte = []
        else:
            return self.handle_war(carte)
        return None
    
    def calculate_probabilities(self):
        wins = {'Player1': 0, 'Player2': 0, 'Draw': 0}
        iterations = 1000

        for _ in range(iterations):
            jeu = WarGame(self.player1, self.player2,self.condition)  # Reset the game
            winner = jeu.simulate_game()
            wins[winner] += 1

        for key in wins:
            wins[key] = wins[key] / iterations

        return wins