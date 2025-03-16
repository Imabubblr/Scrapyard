import tkinter as tk
from tkinter import messagebox

class EvenOddChecker:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill='both', expand=True)

        # Label and entry for user input
        input_label = tk.Label(self.frame, text="Enter a number:", font=("Arial", 12))
        input_label.pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Button to check even/odd
        check_button = tk.Button(self.frame, text="Check Even/Odd", command=self.check_even_odd, font=("Arial", 12))
        check_button.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def check_even_odd(self):
        try:
            number = int(self.entry.get())
            if number % 2 == 0:
                result = "odd"
            else:
                result = "even"
            self.result_label.config(text=f"The number is {result}.", fg="green")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def back_to_menu(self):
        self.frame.pack_forget()  # Hide current frame