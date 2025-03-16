import tkinter as tk
from tkinter import font as tkfont

class ImpossibleRPS:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Create fonts
        self.title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        self.game_font = tkfont.Font(family="Arial", size=16)
        
        # Score tracking
        self.computer_score = 0
        self.player_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        # Game frame
        self.game_frame = tk.Frame(self.parent_frame, bg='white')
        self.game_frame.pack(expand=True)
        
        # Score display
        self.score_label = tk.Label(
            self.game_frame,
            text=f"Computer: {self.computer_score} - Player: {self.player_score}",
            font=self.game_font,
            bg='white'
        )
        self.score_label.pack(pady=10)
        
        # Result display
        self.result_label = tk.Label(
            self.game_frame,
            text="Choose your weapon!",
            font=self.game_font,
            bg='white'
        )
        self.result_label.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.game_frame, bg='white')
        button_frame.pack(pady=20)
        
        # Create choice buttons
        choices = ['Rock', 'Paper', 'Scissors']
        for choice in choices:
            btn = tk.Button(
                button_frame,
                text=choice,
                font=self.game_font,
                width=10,
                command=lambda c=choice: self.play_round(c),
                bg='white',
                relief='solid',
                cursor='hand2'
            )
            btn.pack(side=tk.LEFT, padx=10)
            
            # Add hover effects
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#f0f0f0'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg='white'))
        
        # Reset button
        self.reset_button = tk.Button(
            self.game_frame,
            text="Reset Game",
            font=self.game_font,
            command=self.reset_game,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.reset_button.pack(pady=20)
        
    def play_round(self, player_choice):
        # Computer always wins by choosing the winning move
        computer_choice = self.get_winning_move(player_choice)
        
        # Update result text
        result_text = f"You chose {player_choice}\nComputer chose {computer_choice}\nComputer wins!"
        self.result_label.config(text=result_text)
        
        # Update score
        self.computer_score += 1
        self.score_label.config(text=f"Computer: {self.computer_score} - Player: {self.player_score}")
        
    def get_winning_move(self, player_choice):
        # Returns the move that beats the player's choice
        if player_choice == 'Rock':
            return 'Paper'
        elif player_choice == 'Paper':
            return 'Scissors'
        else:  # Scissors
            return 'Rock'
            
    def reset_game(self):
        self.computer_score = 0
        self.player_score = 0
        self.score_label.config(text=f"Computer: {self.computer_score} - Player: {self.player_score}")
        self.result_label.config(text="Choose your weapon!")