import tkinter as tk
import random

class EscapingButton:
    def __init__(self, parent):
        self.parent = parent
        
        # Create the label
        self.title_label = tk.Label(parent, text="Try to click the button!", font=("Arial", 12, "bold"))
        self.title_label.pack(pady=10)

        # Create a container frame for the canvas
        self.button_size = 60  # Diameter of the circle
        self.container = tk.Frame(parent, width=self.button_size, height=self.button_size,
                                bg=parent.cget('bg'))
        self.container.place(x=200, y=400)
        # Prevent the frame from resizing
        self.container.pack_propagate(False)

        # Create a canvas for the circular button
        self.canvas = tk.Canvas(self.container, width=self.button_size, height=self.button_size, 
                              highlightthickness=0, bg=parent.cget('bg'))
        self.canvas.pack(expand=True)

        # Create the circular button
        self.button = self.canvas.create_oval(2, 2, self.button_size-2, self.button_size-2, 
                                            fill='#ff0000', outline='#cc0000')
        self.button_text = self.canvas.create_text(self.button_size/2, self.button_size/2, 
                                                 text="Click!", fill='white')

        # Bind click and hover events
        self.canvas.bind('<Button-1>', self.button_clicked)
        self.canvas.bind('<Enter>', self.on_hover)
        self.canvas.bind('<Leave>', self.on_leave)

        # Bind mouse motion to move_button function
        parent.bind("<Motion>", self.move_button)

    def button_clicked(self, event=None):
        self.title_label.config(text="Button Clicked!")

    def on_hover(self, event):
        self.canvas.itemconfig(self.button, fill='#ff3333')

    def on_leave(self, event):
        self.canvas.itemconfig(self.button, fill='#ff0000')

    def move_button(self, event):
        """Move the button to a random position if the cursor is close to it"""
        # Get the mouse cursor's position
        mouse_x, mouse_y = event.x_root, event.y_root
        
        # Get the position of the canvas
        button_x = self.container.winfo_rootx()
        button_y = self.container.winfo_rooty()

        # Calculate the distance between the button and the cursor
        distance = ((mouse_x - button_x)**2 + (mouse_y - button_y)**2)**0.5

        # If the distance is less than a threshold (e.g., 100 pixels), move the button
        if distance < 100:  # Threshold for moving the button
            # Get the parent's width and height
            window_width = self.parent.winfo_width()
            window_height = self.parent.winfo_height()

            # Ensure that the button will stay within the boundaries
            max_x = window_width - self.button_size
            max_y = window_height - self.button_size

            # Try random positions until we find one that's at least 250px away
            while True:
                new_x = random.randint(0, max_x)
                new_y = random.randint(0, max_y)

                # Calculate the distance from the previous position
                dist = ((new_x - button_x) ** 2 + (new_y - button_y) ** 2) ** 0.5

                # If the new position is far enough and within bounds, move the button
                if dist >= 250:  # minimum distance of 250px
                    self.container.place(x=new_x, y=new_y)
                    break