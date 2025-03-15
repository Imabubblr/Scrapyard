import tkinter as tk
from tkinter import font as tkfont

class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun and Stupid Projects")
        
        # Set minimum window size
        MIN_WIDTH = 600
        MIN_HEIGHT = 400
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        
        # Set default window size (smaller than fullscreen)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        default_width = min(int(screen_width * 0.5), 1200)  # 75% of screen width or 1200px
        default_height = min(int(screen_height * 0.6), 900) # 75% of screen height or 900px
        
        # Center the window
        x = (screen_width - default_width) // 2
        y = (screen_height - default_height) // 2
        
        self.root.geometry(f"{default_width}x{default_height}+{x}+{y}")
        self.root.configure(bg='white')
        
        # Make the window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create custom font with dynamic sizing
        title_size = min(36, screen_height // 20)  # Scale title font
        menu_size = min(24, screen_height // 30)   # Scale menu font
        self.title_font = tkfont.Font(family="Arial", size=title_size, weight="bold")
        self.menu_font = tkfont.Font(family="Arial", size=menu_size)
        
        # Create a canvas with scrollbar
        self.canvas = tk.Canvas(root, bg='white', highlightthickness=0)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='white')

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Calculate dynamic button width based on screen size
        canvas_width = int(default_width * 0.8)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=canvas_width)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar with responsive padding
        self.canvas.pack(side="left", fill="both", expand=True, padx=screen_width//40)
        scrollbar.pack(side="right", fill="y")

        # Move title inside scrollable frame with left padding
        title = tk.Label(self.scrollable_frame, text="Fun Projects", font=self.title_font, bg='white', fg='black')
        title.pack(pady=screen_height//20, padx=(10, 0))

        # Enable mousewheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Menu items
        menu_items = [
            "Impossible Rock Paper Scissors",
            "Guess My Birthday",
            "Project 3",
            "Project 4",
            "Project 5",
            "Project 6",
            "Project 7",
            "Project 8",
            "Project 9",
            "Project 10"
        ]
        
        # Calculate button dimensions based on screen size
        button_width = min(30, screen_width // 40)  # Responsive button width
        button_padding = screen_height // 50        # Responsive padding
        
        for item in menu_items:
            # Create a frame for each button to center it
            button_frame = tk.Frame(self.scrollable_frame, bg='white')
            button_frame.pack(fill='x', pady=button_padding, padx=(10, 0))
            
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
                width=button_width,
                command=lambda name=item: self.on_click(name)
            )
            # Center the button in its frame
            menu_button.pack(expand=True)
            
            # Hover effects
            menu_button.bind('<Enter>', lambda e, btn=menu_button: self.on_hover(btn))
            menu_button.bind('<Leave>', lambda e, btn=menu_button: self.on_leave(btn))

        # Bind window resize event
        self.root.bind('<Configure>', self.on_window_resize)

    def on_window_resize(self, event):
        # Update font sizes on window resize
        if event.widget == self.root:
            new_title_size = min(36, event.height // 20)
            new_menu_size = min(24, event.height // 30)
            self.title_font.configure(size=new_title_size)
            self.menu_font.configure(size=new_menu_size)
            
            # Update canvas width
            new_canvas_width = int(event.width * 0.8)
            self.canvas.itemconfig(1, width=new_canvas_width)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def on_hover(self, button):
        button.configure(fg='#0066ff', borderwidth=2)
        
    def on_leave(self, button):
        button.configure(fg='black', borderwidth=1)
        
    def on_click(self, item_name):
        print(f"Clicked: {item_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()
