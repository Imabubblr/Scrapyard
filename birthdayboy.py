import tkinter as tk
from tkinter import font as tkfont

class BirthdayGuesser:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Create fonts
        self.game_font = tkfont.Font(family="Arial", size=16)
        self.question_font = tkfont.Font(family="Arial", size=20)
        
        # Initialize game variables
        self.guessing_month = True  # Start with month
        self.guessing_year = False  # Add year guessing state
        self.min_month = 1
        self.max_month = 12
        self.min_day = 1
        self.max_day = 31
        self.min_year = 0  # Add minimum year
        self.max_year = 4000  # Add maximum year
        self.current_guess = 6  # Start in middle of months
        self.attempts = 0
        self.chosen_month = None
        self.chosen_day = None  # Add chosen day variable
        
        # Month names
        self.months = {
            1: "January", 2: "February", 3: "March", 4: "April",
            5: "May", 6: "June", 7: "July", 8: "August",
            9: "September", 10: "October", 11: "November", 12: "December"
        }
        
        # Days per month
        self.days_in_month = {
            1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        self.create_widgets()
        
    def create_widgets(self):
        # Game frame
        self.game_frame = tk.Frame(self.parent_frame, bg='white')
        self.game_frame.pack(expand=True, fill='both', padx=50)
        
        # Instructions
        self.instructions = tk.Label(
            self.game_frame,
            text="Think of your birthday (month and day).\nI'll guess it!",
            font=self.game_font,
            bg='white',
            wraplength=600
        )
        self.instructions.pack(pady=20)
        
        # Question display
        initial_question = f"Is your birthday in {self.months[self.current_guess]}?"
        self.question_label = tk.Label(
            self.game_frame,
            text=initial_question,
            font=self.question_font,
            bg='white',
            wraplength=600,
            justify='center'
        )
        self.question_label.pack(pady=30)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.game_frame, bg='white')
        self.button_frame.pack(pady=20)
        
        # Earlier/Correct/Later buttons
        self.earlier_button = tk.Button(
            self.button_frame,
            text="Earlier",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("earlier"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.earlier_button.pack(side=tk.LEFT, padx=10)
        
        self.correct_button = tk.Button(
            self.button_frame,
            text="Correct!",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("correct"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.correct_button.pack(side=tk.LEFT, padx=10)
        
        self.later_button = tk.Button(
            self.button_frame,
            text="Later",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("later"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.later_button.pack(side=tk.LEFT, padx=10)
        
        # Result label
        self.result_label = tk.Label(
            self.game_frame,
            text="",
            font=self.question_font,
            bg='white',
            wraplength=600
        )
        self.result_label.pack(pady=20)
        
        # Attempts label
        self.attempts_label = tk.Label(
            self.game_frame,
            text=f"Attempts: {self.attempts}",
            font=self.game_font,
            bg='white'
        )
        self.attempts_label.pack(pady=10)
        
        # Reset button (initially hidden)
        self.reset_button = tk.Button(
            self.game_frame,
            text="Play Again",
            font=self.game_font,
            command=self.reset_game,
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        
        # Add hover effects to buttons
        for btn in [self.earlier_button, self.correct_button, self.later_button, self.reset_button]:
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#f0f0f0'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg='white'))
    
    def process_answer(self, answer):
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        
        if answer == "correct":
            if self.guessing_month:
                self.chosen_month = self.current_guess
                self.guessing_month = False
                self.current_guess = 15  # Start in middle of possible days
                self.max_day = self.days_in_month[self.chosen_month]
                self.make_new_guess()
            elif not self.guessing_year:  # If we're guessing day
                self.chosen_day = self.current_guess
                self.guessing_year = True
                self.current_guess = 1962  # Start with a reasonable middle year
                self.make_new_guess()
            else:  # If we're guessing year
                self.show_result()
        elif answer == "earlier":
            if self.guessing_month:
                self.max_month = self.current_guess - 1
            elif self.guessing_year:
                self.max_year = self.current_guess - 1
            else:
                self.max_day = self.current_guess - 1
            self.make_new_guess()
        else:  # later
            if self.guessing_month:
                self.min_month = self.current_guess + 1
            elif self.guessing_year:
                self.min_year = self.current_guess + 1
            else:
                self.min_day = self.current_guess + 1
            self.make_new_guess()
    
    def make_new_guess(self):
        if self.guessing_month:
            if self.min_month > self.max_month:
                self.question_label.config(text="Something went wrong!\nPlease play again.")
                self.show_reset()
                return
            self.current_guess = (self.min_month + self.max_month) // 2
            self.question_label.config(text=f"Is your birthday in {self.months[self.current_guess]}?")
        elif self.guessing_year:
            if self.min_year > self.max_year:
                self.question_label.config(text="Something went wrong!\nPlease play again.")
                self.show_reset()
                return
            self.current_guess = (self.min_year + self.max_year) // 2
            self.question_label.config(text=f"Were you born in {self.current_guess}?")
        else:
            if self.min_day > self.max_day:
                self.question_label.config(text="Something went wrong!\nPlease play again.")
                self.show_reset()
                return
            self.current_guess = (self.min_day + self.max_day) // 2
            suffix = 'th' if self.current_guess not in [1,21,31] else 'st' if self.current_guess in [1,21,31] else 'nd' if self.current_guess == 2 else 'rd'
            self.question_label.config(text=f"Is your birthday on {self.months[self.chosen_month]} {self.current_guess}{suffix}?")
    
    def show_result(self):
        # Hide question and buttons
        self.question_label.pack_forget()
        self.earlier_button.pack_forget()
        self.correct_button.pack_forget()
        self.later_button.pack_forget()
        
        # Show result
        suffix = 'th' if self.chosen_day not in [1,21,31] else 'st' if self.chosen_day in [1,21,31] else 'nd' if self.chosen_day == 2 else 'rd'
        self.result_label.config(
            text=f"I got it! Your birthday is {self.months[self.chosen_month]} {self.chosen_day}{suffix}, {self.current_guess}!\nI found it in {self.attempts} attempts!"
        )
        self.show_reset()
    
    def show_reset(self):
        self.reset_button.pack(pady=20)
    
    def reset_game(self):
        # Reset variables
        self.guessing_month = True
        self.guessing_year = False
        self.min_month = 1
        self.max_month = 12
        self.min_day = 1
        self.max_day = 31
        self.min_year = 0
        self.max_year = 5000
        self.current_guess = 6
        self.attempts = 0
        self.chosen_month = None
        self.chosen_day = None
        
        # Reset UI
        self.result_label.config(text="")
        self.reset_button.pack_forget()
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        
        # Show question again
        self.question_label.config(text=f"Is your birthday in {self.months[self.current_guess]}?")
        self.question_label.pack(pady=30)
        
        # Destroy old button frame and all its children
        self.button_frame.destroy()
        
        # Create new button frame
        self.button_frame = tk.Frame(self.game_frame, bg='white')
        self.button_frame.pack(pady=20)
        
        # Create new buttons
        self.earlier_button = tk.Button(
            self.button_frame,
            text="Earlier",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("earlier"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.earlier_button.pack(side=tk.LEFT, padx=10)
        
        self.correct_button = tk.Button(
            self.button_frame,
            text="Correct!",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("correct"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.correct_button.pack(side=tk.LEFT, padx=10)
        
        self.later_button = tk.Button(
            self.button_frame,
            text="Later",
            font=self.game_font,
            width=10,
            command=lambda: self.process_answer("later"),
            bg='white',
            relief='solid',
            cursor='hand2'
        )
        self.later_button.pack(side=tk.LEFT, padx=10)
        
        # Add hover effects to new buttons
        for btn in [self.earlier_button, self.correct_button, self.later_button]:
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#f0f0f0'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg='white')) 