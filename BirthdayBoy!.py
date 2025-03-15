import tkinter as tk
from datetime import datetime, timedelta
import random

# Initialize guess range
low = datetime(1900, 1, 1)
high = datetime.today()

def random_guess():
    return low + timedelta(days=random.randint(0, (high - low).days))

guess = random_guess()

def update_guess(direction):
    global low, high, guess
    if direction == "older":
        high = guess
    elif direction == "younger":
        low = guess
    guess = random_guess()
    guess_label.config(text=f"Is your birthday {guess.strftime('%Y-%m-%d')}?")

# Create main window
root = tk.Tk()
root.title("Random Birthday Guesser")
root.geometry("350x200")

# Title label
title_label = tk.Label(root, text="I will guess your birthday!", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Guess label
guess_label = tk.Label(root, text=f"Is your birthday {guess.strftime('%Y-%m-%d')}?", font=("Arial", 10))
guess_label.pack(pady=10)

# Buttons
older_button = tk.Button(root, text="earlier", command=lambda: update_guess("older"))
younger_button = tk.Button(root, text="later", command=lambda: update_guess("younger"))
correct_button = tk.Button(root, text="Correct!", command=lambda: guess_label.config(text="I guessed it! 🎉"))

older_button.pack(pady=5)
younger_button.pack(pady=5)
correct_button.pack(pady=5)

# Run the application
root.mainloop()