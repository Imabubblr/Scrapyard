import tkinter as tk
import random

class PointlessClicker:
    def __init__(self, parent_frame):
        
        self.n = 0  # Initial count value
        self.parent = parent_frame
        
        # Create main game frame with proper sizing
        self.game_frame = tk.Frame(self.parent, bg='white')
        self.game_frame.pack(expand=True, fill='both')
        
        # Create a container frame for centered content
        self.container = tk.Frame(self.game_frame, bg='white')
        self.container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Create the label to display the number of clicks
        self.prompt_label = tk.Label(
            self.container,
            text="Click fast",
            font=("Arial", 24),  # Increased font size
            bg='white'
        )
        self.prompt_label.pack(pady=20)
        
        # Create a button
        self.click_button = tk.Button(
            self.container,
            text="Click me",
            command=self.clicky,
            width=25,
            height=4,
            font=("Arial", 20),  # Increased font size
            bg='white',
            fg='black',
            cursor='hand2',
            relief='solid',
            borderwidth=1,
            activebackground='#f0f0f0',
            activeforeground='#0066ff'
        )
        self.click_button.pack(pady=20)
        
        # Stats label
        self.stats_label = tk.Label(
            self.container,
            text="Total Clicks: 0",
            font=("Arial", 18),
            bg='white'
        )
        self.stats_label.pack(pady=20)
        
        # Add hover effects
        self.click_button.bind('<Enter>', lambda e: self.on_hover(self.click_button))
        self.click_button.bind('<Leave>', lambda e: self.on_leave(self.click_button))

    def clicky(self):
        self.n += 1
        
        # Make Ultra Clicks rarer (10% chance)
        click_type = random.choices(
            ["super", "mega", "ultra", "big", "soft"],
            weights=[25, 25, 10, 20, 20]
        )[0]
            
        self.stats_label.config(text=f"Total Clicks: {self.n}")

    def on_hover(self, button):
        button.configure(fg='#0066ff', borderwidth=2)
        
    def on_leave(self, button):
        button.configure(fg='black', borderwidth=1)

# Only create window if running standalone
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pointless Clicker")
    root.geometry("900x700")  # Match the main window size
    root.configure(bg='white')
    app = PointlessClicker(root)
    root.mainloop()