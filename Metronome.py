import tkinter as tk
import random
import pygame

# Initialize the pygame mixer for playing sounds
pygame.mixer.init()

class BrokenMetronome:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Initialize variables
        self.current_tempo = 500
        self.is_running = False
        
        # Create the main content frame
        self.create_widgets()
        
    def create_widgets(self):
        # Create a label to show the text
        self.label = tk.Label(
            self.parent_frame,
            text="Click Start to begin...",
            font=("Helvetica", 24),
            bg='white'
        )
        self.label.pack(pady=20)
        
        # Create start/stop button
        self.toggle_button = tk.Button(
            self.parent_frame,
            text="Start",
            font=("Helvetica", 16),
            command=self.toggle_metronome,
            bg='white',
            relief='solid',
            borderwidth=1
        )
        self.toggle_button.pack(pady=10)
        
    def print_click(self):
        if not self.is_running:
            return
        
        # Change the background color of the parent frame
        self.parent_frame.config(bg=self.random_color())
        self.label.config(bg=self.parent_frame.cget('bg'))
        
        # Play a click sound
        self.play_sound()
        
        # Schedule the next "click" based on the current tempo
        self.parent_frame.after(self.current_tempo, self.print_click)
        
        # After a random interval, change the tempo
        self.parent_frame.after(random.randint(10000, 20000), self.change_tempo)
        
    def random_color(self):
        return f'#{random.randint(0, 0xFFFFFF):06x}'
        
    def play_sound(self):
        try:
            # Use relative path for the sound file in the same folder
            sound_path = "metronome-tempo-single-sound_G_major.wav"
            pygame.mixer.Sound(sound_path).play()
        except:
            print("Sound file not found")
            
    def change_tempo(self):
        if self.is_running:
            self.current_tempo = random.randint(200, 1000)
            
    def toggle_metronome(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.toggle_button.config(text="Stop")
            self.parent_frame.after(random.randint(1, 20) * 50, self.print_click)
        else:
            self.toggle_button.config(text="Start")
            self.parent_frame.config(bg='white')
            self.label.config(bg='white', text="Click Start to begin...")

# The code below is the standalone version, will only run if this file is run directly
if __name__ == "__main__":
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Random Tempo Click Printer") 

    # Create a label to show the text
    label = tk.Label(root, text="Waiting for the first click...", font=("Helvetica", 16))
    label.pack(pady=20)

    # Define the tempo interval in milliseconds (initially set to a reasonable value)
    current_tempo = 500  # This means the sound will play every 500 milliseconds

    def print_click():
        # Update the label with the text "click"
        label.config(text="click")
        
        # Change the background color of the window to a random color
        root.config(bg=f'#{random.randint(0, 0xFFFFFF):06x}')
        
        # Play a click sound
        sound_path = "metronome-tempo-single-sound_G_major.wav"
        pygame.mixer.Sound(sound_path).play()

        # Schedule the next "click" based on the current tempo
        root.after(current_tempo, print_click)

        # After a random interval (between 3 and 7 seconds), change the tempo
        root.after(random.randint(3000, 7000), change_tempo)

    def change_tempo():
        global current_tempo
        # Change the tempo (interval) to a random value between 200ms and 1000ms
        current_tempo = random.randint(200, 1000)

    # Start the click loop after a random initial delay
    root.after(random.randint(1, 20) * 50, print_click)

    # Run the Tkinter event loop
    root.mainloop()