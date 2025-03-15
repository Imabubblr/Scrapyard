import tkinter as tk

def play_game(user_choice):
    if user_choice in ["1", "Rock", "rock", "roc"]:
        result_label.config(text="I choose Paper\nI win, I always win!")
    elif user_choice in ["2", "paper", "Papier", "Paper", "paaper"]:
        result_label.config(text="I choose Scissors\nI win, I always win!")
    elif user_choice in ["3", "scissors", "Scissors", "scisors"]:
        result_label.config(text="I choose Rock\nI win, I always win!")
    else:
        result_label.config(text="Invalid choice! Try again.")
    
    # Clear the result text after 1 second
    root.after(1000, lambda: result_label.config(text=""))

# Create the main window
root = tk.Tk()
root.title("Unbeatable Rock Paper Scissors")
root.geometry("300x200")

# Create buttons
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()