import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class ImpracticalTodoList:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Create fonts
        self.game_font = tkfont.Font(family="Arial", size=16)
        self.title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        self.main_frame = tk.Frame(self.parent_frame, bg='white')
        self.main_frame.pack(expand=True, fill='both', padx=50)
        
        # Instructions
        self.instructions = tk.Label(
            self.main_frame,
            text="Add tasks to your list... but beware, this to-do list has a mind of its own!",
            font=self.game_font,
            bg='white',
            wraplength=600
        )
        self.instructions.pack(pady=20)
        
        # Task entry
        self.task_entry = tk.Entry(
            self.main_frame,
            font=self.game_font,
            width=40,
            relief='solid',
            bg='white'
        )
        self.task_entry.pack(pady=20)
        
        # Add task button
        self.add_button = tk.Button(
            self.main_frame,
            text="Add Task",
            font=self.game_font,
            command=self.add_task,
            bg='white',
            relief='solid',
            cursor='hand2',
            width=15
        )
        self.add_button.pack(pady=10)
        
        # Task listbox
        self.listbox = tk.Listbox(
            self.main_frame,
            font=self.game_font,
            width=40,
            height=4,
            relief='solid',
            bg='white',
            selectmode='single'
        )
        self.listbox.pack(pady=20)
        
        # Save button (which actually clears the list)
        self.save_button = tk.Button(
            self.main_frame,
            text="Save List",
            font=self.game_font,
            command=self.clear_list,
            bg='white',
            relief='solid',
            cursor='hand2',
            width=15
        )
        self.save_button.pack(pady=10)
        
        # Add hover effects to buttons
        for btn in [self.add_button, self.save_button]:
            btn.bind('<Enter>', lambda e, b=btn: b.configure(bg='#f0f0f0'))
            btn.bind('<Leave>', lambda e, b=btn: b.configure(bg='white'))
        
        # Add Enter key binding for task entry
        self.task_entry.bind('<Return>', lambda e: self.add_task())
    
    def add_task(self):
        # Delete the first task if there are any tasks
        if self.listbox.size() > 0:
            self.listbox.delete(0)
        
        # Add new task
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Warning",
                "Task cannot be empty!",
                parent=self.parent_frame
            )
    
    def clear_list(self):
        self.listbox.delete(0, tk.END)
        messagebox.showinfo(
            "Saved!",
            "Your tasks have been successfully... forgotten!",
            parent=self.parent_frame
        )