import tkinter as tk
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Load sound files with fixed paths
click_sound = pygame.mixer.Sound(r"C:\Users\shujianzhai\Downloads\mouse-click-104737.wav")
explosion_sound = pygame.mixer.Sound(r"C:\Users\shujianzhai\Downloads\explosion-312361.mp3")  # Fixed file extension

n = 0  # Initial count value
root = tk.Tk()
root.title("Click it")
root.geometry("400x300")

def clicky():
    global n  
    n += 1  

    # Make Ultra Clicks rarer (10% chance)
    click_type = random.choices(
        ["super", "mega", "ultra", "big", "soft"],
        weights=[25, 25, 10, 20, 20]  
    )[0]

    if click_type == "ultra":
        explosion_sound.play()
        prompt_label.config(text=f"🔥 Ultra Click! Total Clicks: {n}")
    else:
        click_sound.play()
        prompt_label.config(text=f"{click_type.capitalize()} Click! Total Clicks: {n}")

# Create the label to display the number of clicks
prompt_label = tk.Label(root, text="Click fast", font=("Arial", 12))
prompt_label.pack(pady=10)

# Create a button
yesbutton = tk.Button(root, text="Click me", command=clicky, width=20, height=3, font=("Arial", 14))
yesbutton.pack(pady=10)

root.mainloop()