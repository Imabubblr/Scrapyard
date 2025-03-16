import tkinter as tk
import random
from datetime import datetime

# Generate a random month and day
random_month = random.randint(1, 12)
random_day = random.randint(1, 28)  # Ensures valid dates

# Get today's date
today = datetime.today()

# Convert month number to month name
month_name = datetime(today.year, random_month, 1).strftime("%B")

# Compare with today's month and day
if (random_month, random_day) != (today.month, today.day):
    result_text = f"Today is not {month_name} {random_day}"
else:
    result_text = f"Today is {month_name} {random_day}"

# Create main window
root = tk.Tk()
root.title("Random Date Checker")
root.geometry("300x100")

# Display result
result_label = tk.Label(root, text=result_text, font=("Arial", 12))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()