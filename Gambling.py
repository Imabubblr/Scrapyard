import tkinter as tk
import random
import time

class GamblingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gambling Game")
        
        self.money = 10000
        self.f = False
        
        # Create the GUI elements
        self.balance_label = tk.Label(root, text=f"Your balance: ${self.money}")
        self.balance_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.bet_label = tk.Label(root, text="Enter your gamble amount:")
        self.bet_label.pack(pady=5)

        self.bet_entry = tk.Entry(root)
        self.bet_entry.pack(pady=5)

        self.gamble_button = tk.Button(root, text="Gamble", state=tk.DISABLED, command=self.gamble)
        self.gamble_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=10)

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
        self.root.after(1000, self.check_result, item1, item2, item3, amount)

    def check_result(self, item1, item2, item3, amount):
        """Check the result of the gamble."""
        # Win condition: all items are the same
        if item1 == item2 == item3:
            win_amount = amount * 10
            self.money += win_amount
            self.result_label.config(text=f"You win! You won: ${win_amount}\nYour new balance: ${self.money}")
        else:
            self.money -= amount
            self.result_label.config(text=f"You lose! You lost: ${amount}\nYour new balance: ${self.money}")
        
        # Update balance
        self.update_balance_label()

        # Disable betting if out of money
        if self.money <= 0:
            self.result_label.config(text="You're out of money! Game Over!")
            self.gamble_button.config(state=tk.DISABLED)

    def update_balance_label(self):
        """Update the balance label to reflect the current balance."""
        self.balance_label.config(text=f"Your balance: ${self.money}")

    def quit_game(self):
        """Quit the game."""
        self.root.quit()

# Set up the Tkinter window
root = tk.Tk()
game = GamblingGame(root)
root.mainloop()