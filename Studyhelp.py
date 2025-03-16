import tkinter as tk

class StudyGuide:
    def __init__(self, parent):
        self.parent = parent
        
        # Create input label and entry box
        self.prompt_label = tk.Label(parent, text="Welcome to the advanced study guide!\nWhat do you need help with?", 
                                   font=("Arial", 12))
        self.prompt_label.pack(pady=10)

        self.entry = tk.Entry(parent, width=50)
        self.entry.pack(pady=5)

        # Create submit button
        self.submit_button = tk.Button(parent, text="Submit", command=self.respond)
        self.submit_button.pack(pady=5)

        # Create response label
        self.response_label = tk.Label(parent, text="", font=("Arial", 12), fg="red")
        self.response_label.pack(pady=10)

    def animate_dots(self, count=0):
        dots = "." * (count % 4)  # Cycle through '.', '..', '...', ''
        self.response_label.config(text=f"Thinking{dots}")
        if count < 10:  # Run the animation for a short period
            self.parent.after(300, lambda: self.animate_dots(count + 1))
        else:
            self.response_label.config(text="I got it!\nGo to https://chatgpt.com to solve your problem")

    def respond(self):
        self.response_label.config(text="Thinking")  # Initial text
        self.animate_dots()  # Start the animation
