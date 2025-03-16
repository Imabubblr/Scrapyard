import tkinter as tk
import random
from datetime import datetime

class DateChecker:
    def __init__(self, parent):
        self.parent = parent
        
        # Generate the initial random month and day
        self.generate_random_date()

        # Now create the widgets after result_text is defined
        self.create_widgets()

    def generate_random_date(self):
        # Generate a random month and day
        self.random_month = random.randint(1, 12)
        self.random_day = random.randint(1, 28)  # Ensures valid dates

        # Get today's date
        self.today = datetime.today()

        # Convert month number to month name
        self.month_name = datetime(self.today.year, self.random_month, 1).strftime("%B")

        # Compare with today's month and day
        if (self.random_month, self.random_day) != (self.today.month, self.today.day):
            self.result_text = f"Today is not {self.month_name} {self.random_day}"
        else:
            self.result_text = f"Today is {self.month_name} {self.random_day}"

    def create_widgets(self):
        # Display result
        self.result_label = tk.Label(self.parent, text=self.result_text, font=("Arial", 14))
        self.result_label.pack(pady=(30, 0))  # Adjust the pady to move it higher on the screen

        # Create a button to check again
        check_again_button = tk.Button(
            self.parent,
            text="Check Again",
            font=("Arial", 12),
            command=self.check_again
        )
        check_again_button.pack(pady=(30, 0))  # Add some padding above the button

    def check_again(self):
        # Generate a new random date and update the result label
        self.generate_random_date()
        self.result_label.config(text=self.result_text)  # Update the label with the new result

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Date Checker")
    root.geometry("300x150")  # Increased height to accommodate the button
    app = DateChecker(root)
    root.mainloop()
