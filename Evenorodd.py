import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    try:
        # Get the number from the entry field
        number = int(entry.get())

        # Incorrect logic: Always return the opposite of the correct result
        if number % 2 == 0:
            result = "odd"  # Incorrect result for even numbers
        else:
            result = "even"  # Incorrect result for odd numbers

        # Display the incorrect result
        result_label.config(text=f"The number is {result}.", fg="red")
    except ValueError:
        # Handle invalid input (non-integer values)
        messagebox.showerror("Error", "Please enter a valid integer!")

# Create the main window
root = tk.Tk()
root.title("Incorrect Even/Odd Checker")
root.geometry("500x250")

# Label and entry for user input
input_label = tk.Label(root, text="Enter a number:", font=("Arial", 12))
input_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Button to check even/odd
check_button = tk.Button(root, text="Check Even/Odd", command=check_even_odd, font=("Arial", 12))
check_button.pack(pady=10)

# Label to display the (incorrect) result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()