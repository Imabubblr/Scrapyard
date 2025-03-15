import tkinter as tk
import random

def move_button(event):
    """Move the button to a random position if the cursor is close to it, ensuring it's at least 250 pixels away from the last position."""
    # Get the mouse cursor's position
    mouse_x, mouse_y = event.x_root, event.y_root
    
    # Get the position of the button
    button_x, button_y = older_button.winfo_rootx(), older_button.winfo_rooty()

    # Calculate the distance between the button and the cursor
    distance = ((mouse_x - button_x)**2 + (mouse_y - button_y)**2)**0.5

    # If the distance is less than a threshold (e.g., 100 pixels), move the button
    if distance < 100:  # Threshold for moving the button
        # Get the button's dimensions
        button_width = older_button.winfo_width()
        button_height = older_button.winfo_height()

        # Define the minimum distance between the old and new positions (250px)
        min_distance = 250

        # Get the window's width and height (1000x1500)
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        # Ensure that the button will stay within the boundaries of the window
        max_x = window_width - button_width
        max_y = window_height - button_height

        # Try random positions until we find one that's at least 250px away from the last position
        while True:
            new_x = random.randint(0, max_x)
            new_y = random.randint(0, max_y)

            # Calculate the distance from the previous position
            dist = ((new_x - button_x) ** 2 + (new_y - button_y) ** 2) ** 0.5

            # If the new position is far enough and within the window bounds, move the button
            if dist >= min_distance:
                older_button.place(x=new_x, y=new_y)
                break

# Create the main window
root = tk.Tk()
root.title("Click the Button")
root.geometry("1000x1500")  # Set the window size to 1000x1500

# Create the label
title_label = tk.Label(root, text="Click The button", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Create the button and place it in the window initially at a fixed position
older_button = tk.Button(root, text="Click me", command=lambda: title_label.config(text="Button Clicked!"))
older_button.place(x=200, y=400)  # Initial position

# Bind mouse motion to move_button function
root.bind("<Motion>", move_button)

# Run the Tkinter event loop
root.mainloop()