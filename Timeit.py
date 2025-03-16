import tkinter as tk
import time
import random

class StopwatchApp:
    def __init__(self, parent_frame):
        # Initialize time variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.stopped_once = False
        self.fake_time = 0
        self.money = 1000.00

        # Create main container frame
        self.container = tk.Frame(parent_frame, bg='white')
        self.container.pack(fill='both', expand=True)

        # Create UI components
        self.time_display = tk.Label(
            self.container, 
            text="00:00.000", 
            font=("Arial", 30),
            bg='white'
        )
        self.time_display.pack(pady=20)

        # Button frame for better organization
        button_frame = tk.Frame(self.container, bg='white')
        button_frame.pack(pady=10)

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            width=10,
            command=self.start,
            font=("Arial", 12),
            bg='white',
            cursor='hand2',
            relief='solid'
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(
            button_frame,
            text="Stop",
            width=10,
            command=self.stop,
            state=tk.DISABLED,
            font=("Arial", 12),
            bg='white',
            cursor='hand2',
            relief='solid'
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            width=10,
            command=self.reset,
            font=("Arial", 12),
            bg='white',
            cursor='hand2',
            relief='solid'
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

        # Result and money labels
        self.result_label = tk.Label(
            self.container,
            text="",
            font=("Arial", 20),
            bg='white'
        )
        self.result_label.pack(pady=20)
        self.result_label.pack_forget()

        self.money_label = tk.Label(
            self.container,
            text=f"Money: ${self.money:.2f}",
            font=("Arial", 14),
            bg='white'
        )
        self.money_label.pack(pady=10)

        # Instructions
        instructions = (
            "Try to stop the timer at exactly 10 seconds!\n"
            "Win up to $50 for getting close,\n"
            "Lose $10 if you're too far off."
        )
        self.instructions_label = tk.Label(
            self.container,
            text=instructions,
            font=("Arial", 12),
            bg='white',
            fg='#666666'
        )
        self.instructions_label.pack(pady=20)

    def update_time(self):
        if self.running:
            # Get the real time that has passed
            real_time = time.time() - self.start_time
            
            # Fake time: Scale it so that each real millisecond counts as 5 milliseconds on the stopwatch
            self.fake_time = real_time * 5  # Make it "run" at 5x the speed

            # Auto-stop at 15 seconds (75 seconds in fake time)
            if self.fake_time >= 15:
                self.stop()
                return

            # Calculate the fake time in seconds and milliseconds
            seconds, milliseconds = divmod(self.fake_time, 1)
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)

            # Format the time string to only show hours:seconds.milliseconds
            time_str = f"{int(hours):02}:{int(seconds):02}.{int(milliseconds * 1000):03}"
            self.time_display.config(text=time_str)

            # Continue updating if the stopwatch is running
            self.container.after(1, self.update_time)

    def check_win_condition(self):
        """Check if the player wins or loses AFTER stopping."""
        difference_from_10 = abs(self.fake_time - 10)

        if difference_from_10 < 0.3:
            # The closer to 10, the more you win (max reward if exactly at 10.000)
            max_reward = 50  # Maximum possible reward
            money_earned = max_reward * (1 - (difference_from_10 / 0.3))  # Scale reward based on closeness
            self.money += money_earned
            self.result_label.config(text="You Win!", fg="green")
        
        else:
            # Lose a flat $10 if you're too far from 10.000
            self.money -= 10
            self.result_label.config(text="You Lose!", fg="red")

        # Update the money display
        self.money_label.config(text=f"Money: ${self.money:.2f}")

        # Show the result message
        self.result_label.pack()

    def start(self):
        if not self.running:  # Start the stopwatch if it's not already running
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)  # Disable the Start button after starting
            self.stop_button.config(state=tk.NORMAL)  # Enable the Stop button after starting

    def stop(self):
        if not self.stopped_once:  # Only allow stopping once
            self.running = False
            self.stopped_once = True  # Set the flag that the stopwatch has been stopped
            self.start_button.config(state=tk.DISABLED)  # Disable the Start button after stopping
            self.stop_button.config(state=tk.DISABLED)  # Disable the Stop button after stopping
            
            self.check_win_condition()  # Now check win/lose condition only AFTER stopping

    def reset(self):
        """Reset the stopwatch without resetting money."""
        self.running = False
        self.stopped_once = False  # Allow the stopwatch to be restarted
        self.elapsed_time = 0
        self.fake_time = 0  # Reset fake time as well
        self.time_display.config(text="00:00.000")
        self.start_button.config(text="Start", state=tk.NORMAL)  # Enable Start button
        self.stop_button.config(state=tk.DISABLED)  # Disable Stop button until Start is pressed
        self.result_label.pack_forget()  # Hide the result message
        
        # Keep the money value as is (do not reset it)
        self.money_label.config(text=f"Money: ${self.money:.2f}")  # Update money display