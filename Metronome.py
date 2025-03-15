import tkinter as tk
import random
import pygame

# Initialize the pygame mixer for playing sounds
pygame.mixer.init()

# Define the tempo interval in milliseconds (initially set to a reasonable value)
current_tempo = 500  # This means the sound will play every 500 milliseconds

def print_click():
    # Update the label with the text "click"
    label.config(text="click")
    
    # Change the background color of the window to a random color
    root.config(bg=random_color())
    
    # Play a click sound
    play_sound()

    # Schedule the next "click" based on the current tempo
    root.after(current_tempo, print_click)

    # After a random interval (between 3 and 7 seconds), change the tempo
    root.after(random.randint(3000, 7000), change_tempo)

def random_color():
    # Return a random color in hex format
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def play_sound():
    # Play a short sound (ensure you have a sound file in the specified location)
    sound_path = r"c:\Users\shujianzhai\Desktop\roy's things\metronome-tempo-single-sound_G_major.wav"  # Raw string for file path
    pygame.mixer.Sound(sound_path).play()

def change_tempo():
    global current_tempo
    # Change the tempo (interval) to a random value between 200ms and 1000ms
    current_tempo = random.randint(200, 1000)

# Create the Tkinter window
root = tk.Tk()
root.title("Random Tempo Click Printer") 

# Create a label to show the text
label = tk.Label(root, text="Waiting for the first click...", font=("Helvetica", 16))
label.pack(pady=20)

# Start the click loop after a random initial delay
root.after(random.randint(1, 20) * 50, print_click)

# Run the Tkinter event loop
root.mainloop()