import tkinter as tk
from tkinter import messagebox

def add_task():
    if listbox.size() > 0: 
        listbox.delete(0)
    
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def clear_list():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

clear_button = tk.Button(root, text="Save", command=clear_list)
clear_button.pack()

root.mainloop()