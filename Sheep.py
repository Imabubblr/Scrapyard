import tkinter as tk
import time

class SheepJumpingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jumping Sheep")
        self.root.geometry("500x300")
        
        self.canvas = tk.Canvas(root, width=500, height=300, bg="lightblue")
        self.canvas.pack()
        
        # Add grass at the bottom
        self.canvas.create_rectangle(0, 250, 500, 300, fill="green", outline="")
        
        # Draw the fence above the grass (adjusted y-coordinate to 230)
        self.fence = self.canvas.create_rectangle(220, 230, 240, 250, fill="saddlebrown")
        self.canvas.create_line(200, 230, 260, 230, width=4, fill="black")
        self.canvas.create_line(200, 240, 260, 240, width=4, fill="black")
        self.canvas.create_line(200, 250, 260, 250, width=4, fill="black")
        
        # Create the sheep (body and head)
        self.sheep_body = self.canvas.create_oval(100, 180, 160, 220, fill="white")
        self.sheep_head = self.canvas.create_oval(150, 190, 170, 210, fill="gray")
        self.sheep_legs = [
            self.canvas.create_line(110, 220, 110, 240, width=4, fill="black"),
            self.canvas.create_line(120, 220, 120, 240, width=4, fill="black"),
            self.canvas.create_line(140, 220, 140, 240, width=4, fill="black"),
            self.canvas.create_line(150, 220, 150, 240, width=4, fill="black"),
        ]
        
        # Jump count tracking
        self.jump_count = 0  # Counter for the number of jumps over the fence
        self.jump_text = None  # Variable to store reference to the jump count text
        
        # Start first jump after a short delay
        self.root.after(1000, self.jump_sheep)

    def jump_sheep(self):
        jump_height = -10  # Increased jump height
        jump_distance = 10
        jump_steps = 10  # More steps for smoother, higher jump
        
        # Move up and forward
        for _ in range(jump_steps):
            self.move_sheep(jump_distance, jump_height)
        
        # Move down and forward
        for _ in range(jump_steps):
            self.move_sheep(jump_distance, -jump_height)
        
        # Check if sheep has crossed the fence
        if self.check_jump_over_fence():
            self.jump_count += 1  # Increment jump count when jumping over fence
        
        # Delete the old jump count if it exists
        if self.jump_text:
            self.canvas.delete(self.jump_text)
        
        # Update the jump count display
        self.jump_text = self.canvas.create_text(200, 100, text=str(self.jump_count), font=("Arial", 12, "bold"), fill="black")
        
        # Show "Sheep" text on landing
        sheep_text = self.canvas.create_text(130, 230, text="Sheep", font=("Arial", 12, "bold"), fill="black")
        self.root.update()
        time.sleep(0.5)
        self.canvas.delete(sheep_text)
        
        # Pause and fade out
        time.sleep(0.5)
        
        # Reset sheep position after fading
        self.reset_sheep()

        # After returning to start, show "Sheep" in a message box
        self.show_sheep_message()

        # Set up the next jump after a brief delay
        self.root.after(1000, self.jump_sheep)

    def move_sheep(self, x, y):
        self.canvas.move(self.sheep_body, x, y)
        self.canvas.move(self.sheep_head, x, y)
        for leg in self.sheep_legs:
            self.canvas.move(leg, x, y)
        self.root.update()
        time.sleep(0.05)

    def check_jump_over_fence(self):
        """Check if the sheep has jumped over the fence."""
        sheep_top = self.canvas.coords(self.sheep_body)[1]  # Get the top y-coordinate of the sheep's body
        return sheep_top < 230  # If the top of the sheep's body is above the fence (y=230), it has jumped over

    def reset_sheep(self):
        self.canvas.itemconfig(self.sheep_body, fill="white")
        self.canvas.itemconfig(self.sheep_head, fill="gray")
        self.canvas.coords(self.sheep_body, 100, 180, 160, 220)
        self.canvas.coords(self.sheep_head, 150, 190, 170, 210)
        for i, (x1, y1, x2, y2) in enumerate([(110, 220, 110, 240), (120, 220, 120, 240), (140, 220, 140, 240), (150, 220, 150, 240)]):
            self.canvas.coords(self.sheep_legs[i], x1, y1, x2, y2)

    def show_sheep_message(self):
        """Show a custom message box with the text 'Sheep' and auto-close after 3 seconds."""
        message_box = tk.Toplevel(self.root)  # Create a new top-level window
        message_box.title("Jumping Sheep")
        
        label = tk.Label(message_box, text="Sheep", font=("Arial", 16), padx=20, pady=20)
        label.pack()
        
        # Close the message box after 3 seconds
        message_box.after(3000, message_box.destroy)

root = tk.Tk()
app = SheepJumpingApp(root)
root.mainloop()
