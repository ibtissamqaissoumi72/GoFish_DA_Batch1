import random 
import tkinter as tk
from tkinter import messagebox

# The Card class represents a single card in the game with an animal on it
class Card:
    def __init__(self, animal):
        self.animal = animal  # The type of animal on the card

    def __repr__(self):
        return f"{self.animal.capitalize()}"  # Show the animal name neatly when printed

# The Deck class manages the entire deck of cards for the game
class Deck:
    def __init__(self):
        animals = ["dog", "cat", "fish", "lion", "butterfly", "bee", "ant", "dinosaur"]  # Types of cards
        self.cards = []  # List to hold all the cards in the deck
        for animal in animals:
            self.cards.extend([Card(animal)] * 4)  # Add 4 cards of each type to the deck
        self.shuffle()  # Randomize the order of the cards

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffle the deck randomly

    def draw_card(self):
        if self.cards:  # Check if there are cards left
            return self.cards.pop()  # Remove and return the top card
        return None  # Return None if no cards are left

# The Player class represents a player in the game
class Player:
    def __init__(self, name):
        self.name = name  # The player's name
        self.hand = []  # Cards currently held by the player

    def add_card(self, card):
        if card:  # Make sure the card is valid
            self.hand.append(card)  # Add the card to the player's hand

    def remove_card(self, card):
        if card in self.hand:  # Check if the player has the card
            self.hand.remove(card)  # Remove the card from the player's hand

    def show_hand(self):
        return [card.animal for card in self.hand]  # Return a list of the animal names in the hand

    def has_set(self):
        # Check if the player has 4 cards of the same type (a set)
        unique_cards = set(self.show_hand())  # Get all unique card types
        for card in unique_cards:
            if self.show_hand().count(card) == 4:  # Count occurrences of each card
                return True  # Return True if a set is found
        return False  # Return False if no sets are found

# The GameLogic class handles the rules and flow of the game
class GameLogic:
    def __init__(self, player, computer, deck, display_widget, text_widget):
        self.deck = deck  # The deck of cards
        self.player = player  # The human player
        self.computer = computer  # The computer opponent
        self.display_widget = display_widget  # Area to show game actions
        self.text_widget = text_widget  # Text box to display game messages
        self.current_player = self.player  # Start with the human player's turn
        self.deal_initial_cards()  # Give both players their starting cards

    def deal_initial_cards(self):
        # Give each player 5 cards to start
        for _ in range(5):
            self.player.add_card(self.deck.draw_card())
            self.computer.add_card(self.deck.draw_card())

    def display_message(self, message):
        # Show a message in the text box
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, message + "\n")
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.yview(tk.END)  # Scroll to the latest message

    def ask_for_card(self, asker, target, card):
        # When a player asks another for a card
        if card in target.hand:  # Check if the target has the requested card
            target.remove_card(card)
            asker.add_card(card)
            self.display_message(f"{target.name} gives {card} to {asker.name}.")
            return True
        else:
            self.display_message(f"{target.name} says: 'Go Fish!'")
            drawn_card = self.deck.draw_card()  # The asker draws a card if the target doesn't have it
            if drawn_card:
                asker.add_card(drawn_card)
                self.display_message(f"{asker.name} draws a card.")
            return False

    def check_winner(self):
        # Check if someone has won (has a set of 4 cards)
        if self.player.has_set():
            self.display_message(f"Congratulations, {self.player.name}! You win!")
            return self.player.name
        elif self.computer.has_set():
            self.display_message(f"{self.computer.name} wins! Better luck next time.")
            return self.computer.name
        return None

    def player_turn(self, requested_card):
        # Handle the human player's turn
        if requested_card in self.player.show_hand():  # Make sure the player asks for a card they have
            self.ask_for_card(self.player, self.computer, requested_card)
            winner = self.check_winner()
            if winner:
                return winner
        else:
            self.display_message("Invalid choice. Please choose a card from your hand.")
        return None

    def computer_turn(self):
        # Handle the computer's turn
        if not self.computer.hand:  # Skip if the computer has no cards
            return None
        requested_card = random.choice(self.computer.hand)  # Randomly pick a card to ask for
        self.display_message(f"{self.computer.name} asks: Do you have a {requested_card}?")
        self.ask_for_card(self.computer, self.player, requested_card)
        return self.check_winner()

    def switch_turn(self):
        # Switch turns between the player and the computer
        self.current_player = self.computer if self.current_player == self.player else self.player

    def start_new_game(self):
        # Reset the game to start over
        self.deck = Deck()
        self.player.hand = []
        self.computer.hand = []
        self.deal_initial_cards()
        self.display_message("\n--- A new game begins! ---")
        return self

# The GameUI class sets up and manages the visual interface of the game
class GameUI:
    def __init__(self, root):
        self.root = root  # The main application window
        self.game = None  # Placeholder for the game logic
        self.setup_ui()  # Create the UI elements

    def setup_ui(self):
        # Create the layout for the game
        self.root.title("Go Fish Game")
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(padx=10, pady=10)

        self.name_label = tk.Label(self.game_frame, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.game_frame)
        self.name_entry.pack()

        self.start_button = tk.Button(self.game_frame, text="Start Game", command=self.start_game_ui)
        self.start_button.pack()

        self.text_widget = tk.Text(self.game_frame, height=10, width=50, state=tk.DISABLED)
        self.text_widget.pack(pady=10)

        self.display_widget = tk.Frame(self.root)
        self.display_widget.pack()

    def start_game_ui(self):
        # Start the game after the player enters their name
        player_name = self.name_entry.get().strip()
        if player_name:
            self.start_button.pack_forget()  # Hide the start button
            player = Player(player_name)
            computer = Player("Computer")
            deck = Deck()
            self.game = GameLogic(player, computer, deck, self.display_widget, self.text_widget)
            self.game.display_message("--- Let's start the Go Fish game! ---")
            self.game.display_message("RULES: Collect 4 matching cards to win.")
            self.player_turn()
        else:
            messagebox.showwarning("Input Error", "Please enter your name!")

    def player_turn(self):
        # Display the player's hand and ask for input
        self.display_message(f"Your hand: {', '.join(self.game.player.show_hand())}")

        def on_submit():
            requested_card = card_entry.get().strip().lower()
            winner = self.game.player_turn(requested_card)
            if winner:
                self.end_game(winner)
            else:
                card_label.pack_forget()
                card_entry.pack_forget()
                submit_button.pack_forget()
                self.game.switch_turn()
                self.computer_turn()

        card_label = tk.Label(self.display_widget, text="Enter the card you want to ask for:")
        card_label.pack()
        card_entry = tk.Entry(self.display_widget)
        card_entry.pack()
        submit_button = tk.Button(self.display_widget, text="Submit", command=on_submit)
        submit_button.pack()

    def computer_turn(self):
        # Let the computer take its turn
        winner = self.game.computer_turn()
        if winner:
            self.end_game(winner)
        else:
            self.player_turn()

    def display_message(self, message):
        self.game.display_message(message)

    def end_game(self, winner):
        # Handle the end of the game
        if messagebox.askyesno("Game Over", f"{winner} wins! Do you want to play again?"):
            self.game = self.game.start_new_game()
            self.player_turn()
        else:
            self.root.quit()

# Start the application
root = tk.Tk()
game_ui = GameUI(root)
root.mainloop()









