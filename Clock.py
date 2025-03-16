import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Time Adjuster")
root.geometry("400x250")

# Initialize hour, minute, and AM/PM variables
hour = 1
minute = 0
is_pm = False  # False = AM, True = PM

# Function to update the time display
def update_time_display():
    # Update the time label
    time_label.config(text=f"{hour:02d}:{minute:02d} {'PM' if is_pm else 'AM'}")
    
    # Check if the clock matches the current time
    check_current_time()

# Function to check if the clock matches the current time
def check_current_time():
    # Get the current system time
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_is_pm = current_hour >= 12  # Determine if current time is PM

    # Convert 24-hour format to 12-hour format
    if current_hour > 12:
        current_hour -= 12
    elif current_hour == 0:
        current_hour = 12

    # Compare the clock time with the current time
    if (hour == current_hour and minute == current_minute and is_pm == current_is_pm):
        status_label.config(text="Time is correct!", fg="green")
    else:
        status_label.config(text="Time is incorrect.", fg="red")

# Function to increment the hour
def changehour():
    global hour
    hour += 1
    if hour == 13:
        hour = 1
    update_time_display()

# Function to decrement the hour
def changehours():
    global hour
    hour -= 1
    if hour == 0:
        hour = 12
    update_time_display()

# Function to increment the minute
def changemin():
    global minute
    minute += 1
    if minute == 60:
        minute = 0
    update_time_display()

# Function to decrement the minute
def changemins():
    global minute
    minute -= 1
    if minute == -1:
        minute = 59
    update_time_display()

# Function to toggle AM/PM
def toggle_am_pm():
    global is_pm
    is_pm = not is_pm
    update_time_display()

# Label to display the current time
time_label = tk.Label(root, text=f"{hour:02d}:{minute:02d} {'PM' if is_pm else 'AM'}", font=("Arial", 24))
time_label.pack(pady=20)

# Label to display the status (correct/incorrect time)
status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=10)

# Buttons for adjusting the hour
hour_frame = tk.Frame(root)
hour_frame.pack()

Up = tk.Button(hour_frame, text="Hour +", command=changehour)
Up.pack(side="left", padx=5)

Down = tk.Button(hour_frame, text="Hour -", command=changehours)
Down.pack(side="left", padx=5)

# Buttons for adjusting the minute
minute_frame = tk.Frame(root)
minute_frame.pack()

MinUp = tk.Button(minute_frame, text="Minute +", command=changemin)
MinUp.pack(side="left", padx=5)

MinDown = tk.Button(minute_frame, text="Minute -", command=changemins)
MinDown.pack(side="left", padx=5)

# Button to toggle AM/PM
am_pm_button = tk.Button(root, text="Toggle AM/PM", command=toggle_am_pm)
am_pm_button.pack(pady=10)

# Initial time check
update_time_display()

root.mainloop()