import tkinter as tk
import random
import time

class GamblingGame:
    def __init__(self, parent_frame):
        self.parent = parent_frame
        self.money = 10000
        self.f = False
        
        # Create game frame with white background
        self.game_frame = tk.Frame(self.parent, bg='white')
        self.game_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Create the GUI elements with consistent styling
        self.balance_label = tk.Label(
            self.game_frame, 
            text=f"Your balance: ${self.money}",
            font=("Arial", 24),
            bg='white'
        )
        self.balance_label.pack(pady=10)
        
        self.start_button = tk.Button(
            self.game_frame,
            text="Start Game",
            font=("Arial", 18),
            command=self.start_game,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.start_button.pack(pady=10)

        self.bet_label = tk.Label(
            self.game_frame,
            text="Enter your gamble amount:",
            font=("Arial", 18),
            bg='white'
        )
        self.bet_label.pack(pady=5)

        self.bet_entry = tk.Entry(
            self.game_frame,
            font=("Arial", 18),
            width=20
        )
        self.bet_entry.pack(pady=5)

        self.gamble_button = tk.Button(
            self.game_frame,
            text="Gamble",
            font=("Arial", 18),
            state=tk.DISABLED,
            command=self.gamble,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.gamble_button.pack(pady=10)

        self.result_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 20),
            bg='white',
            wraplength=500
        )
        self.result_label.pack(pady=20)

    def start_game(self):
        """Start the game."""
        self.f = True
        self.update_balance_label()
        self.result_label.config(text="Welcome! Start by entering your bet.")
        self.bet_entry.config(state=tk.NORMAL)
        self.gamble_button.config(state=tk.NORMAL)

    def gamble(self):
        """Simulate the gamble."""
        try:
            amount = int(self.bet_entry.get())
            if amount <= 0:
                self.result_label.config(text="Please enter a valid positive amount!")
                return
            if amount > self.money:
                self.result_label.config(text="You don't have enough money. Betting all-in!")
                amount = self.money  # All-in if they try to bet more than they have
        except ValueError:
            self.result_label.config(text="Please enter a valid number!")
            return

        # Simulate the random item selection
        item1 = random.randint(1, 4)
        item2 = random.randint(1, 4)
        item3 = random.randint(1, 4)

        # Show the drawn numbers
        self.result_label.config(text=f"Items drawn: {item1}  {item2}  {item3}")

        # Simulate a pause to show suspense
        self.parent.after(1000, self.check_result, item1, item2, item3, amount)

    def check_result(self, item1, item2, item3, amount):
        """Check the result of the gamble."""
        # Win condition: all items are the same
        if item1 == item2 == item3:
            win_amount = amount * 10
            self.money += win_amount
            self.result_label.config(text=f"You win! You won: ${win_amount}\nYour new balance: ${self.money}")
        else:
            self.money -= amount
            self.result_label.config(text=f"You lose! You lost: ${amount}\nHave 3 matching numbers to win\nYour new balance: ${self.money}")
        
        # Update balance
        self.update_balance_label()

        # Disable betting if out of money
        if self.money <= 0:
            self.result_label.config(text="You're out of money! Game Over!")
            self.gamble_button.config(state=tk.DISABLED)

    def update_balance_label(self):
        """Update the balance label to reflect the current balance."""
        self.balance_label.config(text=f"Your balance: ${self.money}")