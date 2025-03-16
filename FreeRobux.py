import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import threading

# Function to simulate the download with changing speed
def simulate_download():
    # Hide the "Yes" button after it's clicked
    start_button.pack_forget()  # This removes the button from the window
    
    download_label.config(text="Downloading.")
    
    total_time = 10  # Total estimated time for a full download (in minutes)
    progress.set(0)
    progress_bar['value'] = 0
    last_progress = 0  # Initialize last_progress to track the previous value

    # Function for animated "Downloading..."
    def animate_download(download_label):
        animation = ["Downloading.", "Downloading..", "Downloading..."]
        i = 0
        while progress.get() < 99:  # While download is still in progress
            download_label.config(text=animation[i % 3])  # Cycle between the three states
            window.update()
            time.sleep(0.5)  # Delay to simulate animation effect
            i += 1

    # Run the animation in a separate thread (this allows the UI to remain responsive)
    threading.Thread(target=animate_download, args=(download_label,), daemon=True).start()

    while True:
        # Start the progress at 0% and increment up to 99% (it will never hit 100%)
        for i in range(last_progress, 99):  # Ensure it never hits 100%
            # Use a random speed multiplier to simulate varying download speeds
            download_speed = random.uniform(0.03, 0.08)  # Slower speed between 3% to 8% per iteration
            new_progress = min(i + (i * download_speed), 98)  # Ensure it never goes beyond 99%

            # Ensure the progress only increases
            new_progress = max(last_progress, new_progress)  # Ensure the progress is non-decreasing

            progress.set(new_progress)
            progress_bar['value'] = new_progress
            
            # Display the percentage of completion
            percentage_label.config(text=f"{int(new_progress)}% Completed")
            
            # Update the estimated time remaining dynamically based on progress
            estimated_time_remaining_seconds = (99 - new_progress) * (total_time * 60 / 99)  # Convert to seconds
            hours = int(estimated_time_remaining_seconds // 3600)
            minutes = int((estimated_time_remaining_seconds % 3600) // 60)
            seconds = int(estimated_time_remaining_seconds % 60)
            estimated_time_label.config(text=f"Estimated Time Remaining: {hours}h {minutes}m {seconds}s")
            
            window.update()  # Update the GUI
            time.sleep(0.3)  # Slower speed for download (increased delay between updates)

            # Introduce periodic pauses during the download process
            if new_progress % 10 == 0 and new_progress != 99:  # Pause every 10%
                time.sleep(random.uniform(1, 3))  # Random pause duration (1 to 3 seconds)

            # Update the last_progress value
            last_progress = new_progress

        # After completing 99%, simulate the download completion at 99%
        progress.set(99)  # Set the progress bar to 99%
        progress_bar['value'] = 99
        percentage_label.config(text="99% Completed")
        
        # Set the estimated time remaining to 0 seconds
        estimated_time_label.config(text="Estimated Time Remaining: 0s")
        
        # Show an error message (simulated) after completion
        download_label.config(text="Error: Download failed.")
        
        # Ask the user if they want to reinstall
        reinstall = messagebox.askyesno("Download Failed", "The download failed. Would you like to reinstall the package?")
        
        if reinstall:
            # Simulate reinstall process
            download_label.config(text="Reinstalling...")
            time.sleep(2)  # Simulate time to reinstall
            simulate_download()  # Restart the download process
        else:
            # User chose not to reinstall
            download_label.config(text="Download cancelled.")
            break  # Exit the loop and end the program

# Setting up the tkinter window
window = tk.Tk()
window.title("Free Robux Download")

# Add a label to prompt user
welcome_label = tk.Label(window, text="Would you like free Robux?", font=("Arial", 12))
welcome_label.pack(pady=10)

# Button to start the download process
start_button = tk.Button(window, text="Yes", command=simulate_download, font=("Arial", 12))
start_button.pack(pady=10)

# Label to show download status
download_label = tk.Label(window, text="", font=("Arial", 12))
download_label.pack(pady=10)

# Progress bar widget
progress = tk.IntVar()
progress_bar = ttk.Progressbar(window, length=300, mode='determinate', maximum=100, variable=progress)
progress_bar.pack(pady=10)

# Label to show percentage of completion
percentage_label = tk.Label(window, text="0% Completed", font=("Arial", 10))
percentage_label.pack(pady=10)

# Label to show estimated time remaining
estimated_time_label = tk.Label(window, text="Estimated Time Remaining: 0s", font=("Arial", 10))
estimated_time_label.pack(pady=10)

# Start the tkinter mainloop
window.mainloop()