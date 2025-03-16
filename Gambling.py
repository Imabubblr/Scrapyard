import tkinter as tk
import random
import pygame
import time

class GamblingGame:
    def __init__(self, parent_frame):
        self.parent = parent_frame
        self.money = 10000
        self.f = False
        pygame.mixer.init()
        
        # Create game frame with reduced padding
        self.game_frame = tk.Frame(self.parent, bg='white')
        self.game_frame.pack(expand=True, fill='both', padx=20, pady=10)  # Reduced pady
        
        # Create the GUI elements with smaller fonts and padding
        self.balance_label = tk.Label(
            self.game_frame, 
            text=f"Your balance: ${self.money}",
            font=("Arial", 20),  # Reduced font size
            bg='white',
            fg='black'
        )
        self.balance_label.pack(pady=5)  # Reduced padding

        # Create slot machine display frame with less padding
        self.slot_frame = tk.Frame(self.game_frame, bg='white', pady=10)  # Reduced padding
        self.slot_frame.pack()

        # Create three labels for slot numbers with smaller size
        self.slot_labels = []
        for i in range(3):
            slot = tk.Label(
                self.slot_frame,
                text="0",
                font=("Arial", 36),  # Reduced font size
                width=2,  # Reduced width
                relief='solid',
                bg='white',
                fg='black',
                padx=5  # Reduced padding
            )
            slot.pack(side=tk.LEFT, padx=3)  # Reduced padding
            self.slot_labels.append(slot)

        self.start_button = tk.Button(
            self.game_frame,
            text="Start Game",
            font=("Arial", 14),  # Reduced font size
            command=self.start_game,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.start_button.pack(pady=5)  # Reduced padding

        self.bet_label = tk.Label(
            self.game_frame,
            text="Enter your bet amount:",
            font=("Arial", 14),  # Reduced font size
            bg='white'
        )
        self.bet_label.pack(pady=2)  # Reduced padding

        self.bet_entry = tk.Entry(
            self.game_frame,
            font=("Arial", 14),  # Reduced font size
            width=15  # Reduced width
        )
        self.bet_entry.pack(pady=2)  # Reduced padding

        self.gamble_button = tk.Button(
            self.game_frame,
            text="Spin!",
            font=("Arial", 14),  # Reduced font size
            state=tk.DISABLED,
            command=self.gamble,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.gamble_button.pack(pady=5)  # Reduced padding

        self.result_label = tk.Label(
            self.game_frame,
            text="",
            font=("Arial", 14),  # Reduced font size
            bg='white',
            wraplength=500
        )
        self.result_label.pack(pady=5)  # Reduced padding

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
                self.result_label.config(text="You don't have enough money.")
                return
        except ValueError:
            self.result_label.config(text="Please enter a valid number!")
            return

        # Disable gamble button during animation
        self.gamble_button.config(state=tk.DISABLED)
        
        # Start the slot machine animation
        self.animate_slots(amount)

    def animate_slots(self, amount):
        """Animate the slot machine numbers."""
        spins = 0
        max_spins = 20  # Number of animation frames
        final_numbers = [random.randint(1, 4) for _ in range(3)]
        
        def spin():
            nonlocal spins
            if spins < max_spins:
                # Update each slot with random numbers during animation
                for label in self.slot_labels:
                    label.config(text=str(random.randint(1, 4)))
                spins += 1
                # Schedule next animation frame
                self.parent.after(50, spin)
            else:
                # Show final numbers
                for i, number in enumerate(final_numbers):
                    self.slot_labels[i].config(text=str(number))
                # Check results after animation
                self.check_result(final_numbers[0], final_numbers[1], final_numbers[2], amount)
                self.gamble_button.config(state=tk.NORMAL)

        spin()

    def check_result(self, item1, item2, item3, amount):
        """Check the result of the gamble."""
        if item1 == item2 == item3:
            win_amount = amount * 10
            self.money += win_amount
            self.result_label.config(text=f"🎉 JACKPOT! You won: ${win_amount}")
            self.win_sound.play()
        else:
            self.money -= amount
            self.result_label.config(text=f"Better luck next time! You lost: ${amount}\nMatch 3 numbers to win!")
        
        self.update_balance_label()

        if self.money <= 0:
            self.result_label.config(text="You're out of money! Game Over!")
            self.gamble_button.config(state=tk.DISABLED)

    def update_balance_label(self):
        """Update the balance label to reflect the current balance."""
        self.balance_label.config(text=f"Your balance: ${self.money}")