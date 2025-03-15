import tkinter as tk
from tkinter import font as tkfont

class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Projects")
        self.current_frame = None
        
        # Set minimum window size
        MIN_WIDTH = 800  # Increased minimum width
        MIN_HEIGHT = 600  # Increased minimum height
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        
        # Set fixed window size
        default_width = 900
        default_height = 700
        
        # Center the window
        x = (root.winfo_screenwidth() - default_width) // 2
        y = (root.winfo_screenheight() - default_height) // 2
        
        self.root.geometry(f"{default_width}x{default_height}+{x}+{y}")
        self.root.configure(bg='white')
        
        # Create custom font with fixed sizing
        self.title_font = tkfont.Font(family="Arial", size=36, weight="bold")
        self.menu_font = tkfont.Font(family="Arial", size=24)
        
        # Fixed sizes
        self.canvas_width = 700
        self.button_width = 40
        self.button_padding = 8
        
        # Menu items with their corresponding page titles
        self.menu_items = {
            "Impossible Rock Paper Scissors": "Project 1 Page",
            "Guess Your Birthday": "Project 2 Page",
            "Impractical To-Do List": "Project 3 Page",
            "GAMBLING": "Project 4 Page",
            "Project 5": "Project 5 Page",
            "Project 6": "Project 6 Page",
            "Project 7": "Project 7 Page",
            "Project 8": "Project 8 Page",
            "Project 9": "Project 9 Page",
            "Project 10": "Project 10 Page"
        }
        
        # Create main menu frame
        self.main_menu = self.create_main_menu()
        self.show_frame(self.main_menu)

    def create_main_menu(self):
        # Create the main menu frame
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill='both', expand=True)
        
        # Create a canvas with scrollbar
        canvas = tk.Canvas(main_frame, bg='white', highlightthickness=0)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')

        # Add mouse wheel binding
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))
        # For Linux/Unix systems
        canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        # Make canvas responsive to window size
        canvas.create_window(
            (0, 0),
            window=scrollable_frame,
            anchor="n",
            width=self.root.winfo_width() - 50  # Subtract scrollbar width and padding
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        # Center the canvas in the window
        canvas.pack(side="left", fill="both", expand=True, padx=(20, 0))
        scrollbar.pack(side="right", fill="y", padx=(0, 20))

        # Title with center alignment
        title = tk.Label(scrollable_frame, text="Fun Projects", font=self.title_font, bg='white', fg='black')
        title.pack(pady=40)
        
        # Create buttons
        for item in self.menu_items.keys():
            button_frame = tk.Frame(scrollable_frame, bg='white')
            button_frame.pack(fill='x', pady=self.button_padding)
            
            menu_button = tk.Button(
                button_frame,
                text=item,
                font=self.menu_font,
                bg='white',
                fg='black',
                cursor='hand2',
                relief='solid',
                borderwidth=1,
                activebackground='#f0f0f0',
                activeforeground='#0066ff',
                width=25,
                height=1,
                command=lambda name=item: self.show_project_page(name)
            )
            menu_button.pack(expand=True, pady=5, ipady=5)
            
            menu_button.bind('<Enter>', lambda e, btn=menu_button: self.on_hover(btn))
            menu_button.bind('<Leave>', lambda e, btn=menu_button: self.on_leave(btn))

        # Add window resize binding
        self.root.bind('<Configure>', self.on_window_resize)
            
        return main_frame

    def create_project_page(self, project_name):
        # Create a new frame for the project page
        page_frame = tk.Frame(self.root, bg='white')
        page_frame.pack(fill='both', expand=True)
        
        # Back button at the top
        back_button = tk.Button(
            page_frame,
            text="← Back",
            font=self.menu_font,
            bg='white',
            fg='black',
            cursor='hand2',
            relief='solid',
            borderwidth=1,
            command=lambda: self.show_frame(self.main_menu)
        )
        back_button.pack(anchor='nw', padx=20, pady=20)
        
        # Project title
        title = tk.Label(
            page_frame,
            text=self.menu_items[project_name],
            font=self.title_font,
            bg='white',
            fg='black'
        )
        title.pack(pady=50)
        
        # Add your project-specific content here
        content = tk.Label(
            page_frame,
            text=f"Content for {project_name}",
            font=self.menu_font,
            bg='white',
            fg='black'
        )
        content.pack(expand=True)
        
        return page_frame

    def show_project_page(self, project_name):
        new_page = self.create_project_page(project_name)
        self.show_frame(new_page)

    def show_frame(self, frame):
        # Hide current frame if it exists
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        
        # Show new frame
        frame.pack(fill='both', expand=True)
        self.current_frame = frame

    def on_hover(self, button):
        button.configure(fg='#0066ff', borderwidth=2)
        
    def on_leave(self, button):
        button.configure(fg='black', borderwidth=1)
        
    def on_click(self, item_name):
        print(f"Clicked: {item_name}")

    def on_window_resize(self, event):
        if event.widget == self.root:
            # Update canvas width when window resizes
            for child in self.root.winfo_children():
                if isinstance(child, tk.Frame):
                    for widget in child.winfo_children():
                        if isinstance(widget, tk.Canvas):
                            widget.itemconfig(1, width=event.width - 50)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()
