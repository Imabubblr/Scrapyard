import tkinter as tk
from tkinter import font as tkfont
import random  # Add this at the top with other imports
import colorsys  # Add this import at the top

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
        # self.root.configure(bg='#ffffff')
        
        # Create custom font with fixed sizing
        self.title_font = tkfont.Font(family="Arial", size=36, weight="bold")
        self.menu_font = tkfont.Font(family="Arial", size=24)
        
        # Fixed sizes
        self.canvas_width = 700
        self.button_width = 40
        self.button_padding = 8
        
        # Menu items with their corresponding page titles
        self.menu_items = {
            "Time It": "Time It",
            "Impossible Rock Paper Scissors": "Project 1 Page",
            "Guess Your Birthday": "Project 2 Page",
            "Impractical To-Do List": "Project 3 Page",
            "GAMBLING": "Project 4 Page",
            "Escaping Button": "Project 5 Page",
            "Broken Metronome": "Project 6 Page",
            "Time It": "Project 7 Page",
            "Study Guide": "Project 8 Page",
            "FREE ROBUX!! (REAL)": "Project 9 Page",
            "Pointless Clicker": "Project 10 Page"
        }
        
        # Add color animation variables
        self.hue = 0
        self.color_speed = 0.001
        self.animate_colors()
        
        # Create main menu frame
        self.main_menu = self.create_main_menu()
        self.show_frame(self.main_menu)

    def animate_colors(self):
        # Convert HSV to RGB (hue, 0.3, 1.0 for pastel colors)
        rgb = colorsys.hsv_to_rgb(self.hue, 0.3, 1.0)
        # Convert RGB values to hex color string
        color = '#{:02x}{:02x}{:02x}'.format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )
        
        # Update background colors - modified version
        self.root.configure(bg=color)
        if self.current_frame:
            def update_widget_colors(widget):
                widget.configure(bg=color)
                # Special handling for buttons
                if isinstance(widget, tk.Button):
                    rgb = tuple(widget.winfo_rgb(color))
                    darker_rgb = tuple(max(0, val - 5000) for val in rgb)
                    darker_color = '#{:04x}{:04x}{:04x}'.format(*darker_rgb)
                    widget.configure(bg=color, activebackground=darker_color)
                
                # Recursively update all child widgets
                for child in widget.winfo_children():
                    if isinstance(child, (tk.Frame, tk.Label, tk.Button, tk.Canvas)):
                        update_widget_colors(child)
                        # If it's a canvas, also update its internal frame
                        if isinstance(child, tk.Canvas):
                            for inner_frame in child.winfo_children():
                                update_widget_colors(inner_frame)
            
            # Update the main frame and all its children
            update_widget_colors(self.current_frame)
            
            # Find and update the scrollable frame inside the canvas
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, tk.Canvas):
                    for scrollable_frame in widget.winfo_children():
                        update_widget_colors(scrollable_frame)
        
        # Increment hue value
        self.hue = (self.hue + self.color_speed) % 1.0
        
        # Schedule next animation frame
        self.root.after(50, self.animate_colors)

    def create_main_menu(self):
        # Create the main menu frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True)
        
        # Create a canvas with scrollbar - remove bg='white'
        canvas = tk.Canvas(main_frame, highlightthickness=0)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

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
        title = tk.Label(scrollable_frame, text="Fun Projects", font=self.title_font)
        title.pack(pady=(40, 20))  # Reduced bottom padding
        
        # Random project button
        random_button = tk.Button(
            scrollable_frame,
            text="Random",
            font=self.menu_font,
            fg='#0066ff',
            cursor='hand2',
            relief='solid',
            borderwidth=2,
            activeforeground='#0066ff',
            width=15,
            height=1,
            command=self.show_random_project
        )
        # Configure activebackground dynamically
        random_button.bind('<Enter>', lambda e, btn=random_button: self.on_hover_with_bg(btn))
        random_button.bind('<Leave>', lambda e, btn=random_button: self.on_leave_with_bg(btn))
        random_button.pack(pady=(0, 20))
        
        # Create buttons for projects
        for item in self.menu_items.keys():
            button_frame = tk.Frame(scrollable_frame)
            button_frame.pack(fill='x', pady=self.button_padding)
            
            menu_button = tk.Button(
                button_frame,
                text=item,
                font=self.menu_font,
                fg='black',
                cursor='hand2',
                relief='solid',
                borderwidth=1,
                activeforeground='#0066ff',
                width=25,
                height=1,
                command=lambda name=item: self.show_project_page(name)
            )
            menu_button.pack(expand=True, pady=5, ipady=5)
            
            # Update hover bindings
            menu_button.bind('<Enter>', lambda e, btn=menu_button: self.on_hover_with_bg(btn))
            menu_button.bind('<Leave>', lambda e, btn=menu_button: self.on_leave_with_bg(btn))

        # Add window resize binding
        self.root.bind('<Configure>', self.on_window_resize)
            
        return main_frame

    def create_project_page(self, project_name):
        # Create a new frame for the project page
        page_frame = tk.Frame(self.root)
        page_frame.pack(fill='both', expand=True)
        
        # Back button at the top
        back_button = tk.Button(
            page_frame,
            text="← Back",
            font=self.menu_font,
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
            text=project_name,
            font=self.title_font,
            #bg='white',
            fg='black'
        )
        title.pack(pady=20)
        
        if project_name == "Time It":
            from Timeit import StopwatchApp
            game = StopwatchApp(page_frame)
        elif project_name == "Impossible Rock Paper Scissors":
            from RPS import ImpossibleRPS
            game = ImpossibleRPS(page_frame)
        elif project_name == "Guess Your Birthday":
            from birthdayboy import BirthdayGuesser
            game = BirthdayGuesser(page_frame)
        elif project_name == "Impractical To-Do List":
            from Deletinglist import ImpracticalTodoList
            game = ImpracticalTodoList(page_frame)
        elif project_name == "GAMBLING":
            from Gambling import GamblingGame
            game = GamblingGame(page_frame)
        elif project_name == "Escaping Button":
            from Click_The_Button import EscapingButton
            game = EscapingButton(page_frame)
        elif project_name == "Broken Metronome":
            from Metronome import BrokenMetronome
            game = BrokenMetronome(page_frame)
        elif project_name == "Reflexes Game":
            from Timeit import StopwatchApp
            game = StopwatchApp(page_frame)
        elif project_name == "Study Guide":
            from Studyhelp import StudyGuide
            game = StudyGuide(page_frame)
        elif project_name == "FREE ROBUX!! (REAL)":
            from FreeRobux import FreeRobux
            game = FreeRobux(page_frame)
        elif project_name == "Pointless Clicker":
            from clickyclacky import PointlessClicker
            game = PointlessClicker(page_frame)
        else:
            # Add your project-specific content here
            content = tk.Label(
                page_frame,
                text=f"Content for {project_name}",
                font=self.menu_font,
                #bg='white',
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

    def on_hover_with_bg(self, button):
        button.configure(fg='#0066ff', borderwidth=2)
        # Get current background color from parent
        bg_color = button.master.cget('bg')
        # Make active background slightly darker
        rgb = tuple(button.master.winfo_rgb(bg_color))
        darker_rgb = tuple(max(0, val - 5000) for val in rgb)
        darker_color = '#{:04x}{:04x}{:04x}'.format(*darker_rgb)
        button.configure(activebackground=darker_color)
        
    def on_leave_with_bg(self, button):
        button.configure(fg='black', borderwidth=1)
        # Match background with parent
        bg_color = button.master.cget('bg')
        button.configure(bg=bg_color, activebackground=bg_color)

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

    def show_random_project(self):
        # Choose a random project from the menu items
        random_project = random.choice(list(self.menu_items.keys()))
        self.show_project_page(random_project)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()
