"# GoFish_DA_Batch1" 

- This program is a simple "Go Fish" card game built using Python and Tkinter for the graphical interface, it demonstrates Object-Oriented Programming (OOP) concepts like classes, encapsulation, and modularity. The design adheres to some SOLID principles like Open/Closed Principle and Dependency Inversion Principle to keep the code extensible and maintainable.

Card and Deck Classes 
- `Card` Class:
  - Represents individual cards in the game. Each card has an `animal` attribute (e.g., "dog" or "cat").
  - Uses `__repr__` for a user-friendly display of the card.

- `Deck` Class:
  - Contains a list of 32 cards (4 cards for each of 8 animal types).
  - The `shuffle()` method randomizes the cards.
  - The `draw_card()` method lets players pick a card from the deck.

Player Class 
- Represents each player (human or computer).
- Attributes:
  - `name`: Player’s name.
  - `hand`: List of cards they hold.
- Methods:
  - `add_card()`: Adds a card to the player’s hand.
  - `remove_card()`: Removes a card from their hand.
  - `show_hand()`: Displays the player’s hand.
  - `has_set()`: Checks if the player has a set of 4 matching cards (winning condition).

3 GameLogic Class 
- This class handles all the game rules and interactions.
- Attributes:
  - Tracks the players, the deck, and widgets for display and messages.
  - Alternates between the player and computer turns.
  
- Key Methods
  1. `deal_initial_cards()`* Distributes 5 cards to each player at the start.
  2. `ask_for_card()`: Handles the process of asking for cards between players. If the target player doesn’t have the card, the asker draws from the deck.
  3. `check_winner()`: Determines if any player has won by checking for a set of 4 matching cards.
  4. `switch_turn()`: Alternates between the human and computer.
  5. `start_new_game()`: Resets the game for a new round.

- Principle Used: Open/Closed Principle.
  - The `GameLogic` class can be extended to include more rules or features without modifying its core behavior.

GameUI Class
- Purpos: Handles all graphical interface elements using Tkinter.
- Components:
  1. Setup Screen: Accepts the player's name and starts the game.
  2. Display Widget: Shows messages like turns, actions, and outcomes.
  3. Player Interaction: Lets the player input which card they want to ask for.
  4. Game Flow: Alternates between player and computer turns, updates the display, and checks for a winner.

- Key Principle Used: Dependency Inversion Principle.
  - `GameUI` depends on the `GameLogic` class instead of hardcoding logic directly into the interface, making it easier to modify or reuse.


SOLID Principles in the Code 
- Open/Closed Principle (OCP):
  The `GameLogic` and `GameUI` classes can be extended with new features (e.g., new rules or UI changes) without altering their existing code.
  
- Dependency Inversion Principle (DIP):
  - The `GameUI` class relies on abstractions provided by `GameLogic`, ensuring that game logic and UI are decoupled.


- This project showcases OOP principles and SOLID design, resulting in modular, extensible, and maintainable code.
- The code also uses randomization, user input handling, and clear game rules to create an engaging and interactive experience.
- Invite the teacher to ask specific questions about any part of the code.

