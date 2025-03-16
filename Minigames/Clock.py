import tkinter as tk
from datetime import datetime

class Clock:
    def __init__(self, master):
        self.master = master
        self.hour = 1
        self.minute = 0
        self.is_pm = False  # False = AM, True = PM
        
        self.setup_ui()
        self.update_time_display()

    def setup_ui(self):
        # Label to display the current time
        self.time_label = tk.Label(self.master, text=f"{self.hour:02d}:{self.minute:02d} {'PM' if self.is_pm else 'AM'}", font=("Arial", 24))
        self.time_label.pack(pady=20)

        # Label to display the status (correct/incorrect time)
        self.status_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Buttons for adjusting the hour
        hour_frame = tk.Frame(self.master)
        hour_frame.pack()

        Up = tk.Button(hour_frame, text="Hour +", command=self.changehour, width=12, height=3)
        Up.pack(side="left", padx=5)

        Down = tk.Button(hour_frame, text="Hour -", command=self.changehours, width=12, height=3)
        Down.pack(side="left", padx=5)

        # Buttons for adjusting the minute
        minute_frame = tk.Frame(self.master)
        minute_frame.pack()

        MinUp = tk.Button(minute_frame, text="Minute +", command=self.changemin, width=12, height=3)
        MinUp.pack(side="left", padx=5)

        MinDown = tk.Button(minute_frame, text="Minute -", command=self.changemins, width=12, height=3)
        MinDown.pack(side="left", padx=5)

        # Button to toggle AM/PM
        am_pm_button = tk.Button(self.master, text="Toggle AM/PM", command=self.toggle_am_pm, width=12, height=3)
        am_pm_button.pack(pady=10)

    # Function to update the time display
    def update_time_display(self):
        self.time_label.config(text=f"{self.hour:02d}:{self.minute:02d} {'PM' if self.is_pm else 'AM'}")
        self.check_current_time()

    # Function to check if the clock matches the current time
    def check_current_time(self):
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_is_pm = current_hour >= 12  # Determine if current time is PM

        if current_hour > 12:
            current_hour -= 12
        elif current_hour == 0:
            current_hour = 12

        if (self.hour == current_hour and self.minute == current_minute and self.is_pm == current_is_pm):
            self.status_label.config(text="Time is correct!", fg="green")
        else:
            self.status_label.config(text="Time is incorrect.", fg="red")

    # Function to increment the hour
    def changehour(self):
        self.hour += 1
        if self.hour == 13:
            self.hour = 1
        self.update_time_display()

    # Function to decrement the hour
    def changehours(self):
        self.hour -= 1
        if self.hour == 0:
            self.hour = 12
        self.update_time_display()

    # Function to increment the minute
    def changemin(self):
        self.minute += 1
        if self.minute == 60:
            self.minute = 0
        self.update_time_display()

    # Function to decrement the minute
    def changemins(self):
        self.minute -= 1
        if self.minute == -1:
            self.minute = 59
        self.update_time_display()

    # Function to toggle AM/PM
    def toggle_am_pm(self):
        self.is_pm = not self.is_pm
        self.update_time_display()

if __name__ == "__main__":
    root = tk.Tk()
    clock_app = Clock(root)
    root.mainloop()