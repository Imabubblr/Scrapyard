import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import threading

class FreeRobux:
    def __init__(self, parent):
        self.window = parent
        
        # Create a frame to hold all widgets
        self.frame = tk.Frame(self.window, bg='white')
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Add a label to prompt user
        self.welcome_label = tk.Label(self.frame, text="Would you like free Robux?", font=("Arial", 12), bg='white')
        self.welcome_label.pack(pady=10)

        # Button to start the download process
        self.start_button = tk.Button(self.frame, text="Yes", command=self.simulate_download, font=("Arial", 12))
        self.start_button.pack(pady=10)

        # Label to show download status
        self.download_label = tk.Label(self.frame, text="", font=("Arial", 12), bg='white')
        self.download_label.pack(pady=10)

        # Progress bar widget
        self.progress = tk.IntVar()
        self.progress_bar = ttk.Progressbar(self.frame, length=300, mode='determinate', maximum=100, variable=self.progress)
        self.progress_bar.pack(pady=10)

        # Label to show percentage of completion
        self.percentage_label = tk.Label(self.frame, text="0% Completed", font=("Arial", 10), bg='white')
        self.percentage_label.pack(pady=10)

        # Label to show estimated time remaining
        self.estimated_time_label = tk.Label(self.frame, text="Estimated Time Remaining: 0s", font=("Arial", 10), bg='white')
        self.estimated_time_label.pack(pady=10)

    def simulate_download(self):
        # Hide the "Yes" button after it's clicked
        self.start_button.pack_forget()
        
        self.download_label.config(text="Downloading.")
        
        total_time = 10  # Total estimated time for a full download (in minutes)
        self.progress.set(0)
        self.progress_bar['value'] = 0
        last_progress = 0

        # Function for animated "Downloading..."
        def animate_download():
            animation = ["Downloading.", "Downloading..", "Downloading..."]
            i = 0
            while self.progress.get() < 99:
                self.download_label.config(text=animation[i % 3])
                self.window.update()
                time.sleep(0.5)
                i += 1

        # Run the animation in a separate thread
        threading.Thread(target=animate_download, daemon=True).start()

        while True:
            for i in range(last_progress, 99):
                download_speed = random.uniform(0.03, 0.08)
                new_progress = min(i + (i * download_speed), 98)
                new_progress = max(last_progress, new_progress)

                self.progress.set(new_progress)
                self.progress_bar['value'] = new_progress
                
                self.percentage_label.config(text=f"{int(new_progress)}% Completed")
                
                estimated_time_remaining_seconds = (99 - new_progress) * (total_time * 60 / 99)
                hours = int(estimated_time_remaining_seconds // 3600)
                minutes = int((estimated_time_remaining_seconds % 3600) // 60)
                seconds = int(estimated_time_remaining_seconds % 60)
                self.estimated_time_label.config(text=f"Estimated Time Remaining: {hours}h {minutes}m {seconds}s")
                
                self.window.update()
                time.sleep(0.3)

                if new_progress % 10 == 0 and new_progress != 99:
                    time.sleep(random.uniform(1, 3))

                last_progress = new_progress

            self.progress.set(99)
            self.progress_bar['value'] = 99
            self.percentage_label.config(text="99% Completed")
            self.estimated_time_label.config(text="Estimated Time Remaining: 0s")
            self.download_label.config(text="Error: Download failed.")
            
            reinstall = messagebox.askyesno("Download Failed", "The download failed. Would you like to reinstall the package?")
            
            if reinstall:
                self.download_label.config(text="Reinstalling...")
                time.sleep(2)
                self.simulate_download()
            else:
                self.download_label.config(text="Download cancelled.")
                break