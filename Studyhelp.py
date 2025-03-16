import tkinter as tk

def animate_dots(count=0):
    dots = "." * (count % 4)  # Cycle through '.', '..', '...', ''
    response_label.config(text=f"Thinking{dots}")
    if count < 10:  # Run the animation for a short period
        root.after(300, lambda: animate_dots(count + 1))
    else:
        response_label.config(text="I solved it!\nGo to https://chatgpt.com")

def respond():
    response_label.config(text="Thinking")  # Initial text
    animate_dots()  # Start the animation

# Create main window
root = tk.Tk()
root.title("Advanced Study Guide")
root.geometry("400x200")

# Create input label and entry box
prompt_label = tk.Label(root, text="Welcome to the advanced study guide!\nWhat do you need help with?", font=("Arial", 12))
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=respond)
submit_button.pack(pady=5)

# Create response label
response_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
response_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
