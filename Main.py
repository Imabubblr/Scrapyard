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
        MIN_WIDTH = 800
        MIN_HEIGHT = 600
        self.root.minsize(MIN_WIDTH, MIN_HEIGHT)
        
        # Set fixed window size
        default_width = 900
        default_height = 700
        
        # Center the window
        x = (root.winfo_screenwidth() - default_width) // 2
        y = (root.winfo_screenheight() - default_height) // 2
        
        self.root.geometry(f"{default_width}x{default_height}+{x}+{y}")
        
        # Add dark mode settings first
        self.dark_mode = False
        self.light_theme = {
            'bg': '#ffffff',
            'fg': '#000000',
            'button_fg': '#0066ff',
            'subtitle_fg': '#555555',
            'shadow': '#cccccc',
            'border': '#dddddd'  # Light gray border
        }
        self.dark_theme = {
            'bg': '#1a1a1a',
            'fg': '#ffffff',
            'button_fg': '#66b3ff',
            'subtitle_fg': '#aaaaaa',
            'shadow': '#111111',
            'border': '#333333'  # Dark gray border
        }
        self.current_theme = self.light_theme
        
        # Add gradient settings
        self.gradient_colors = ['#FF6B6B', '#4ECDC4']
        self.gradient_speed = 0.002
        self.color_speed = self.gradient_speed
        
        # Update font settings
        self.title_font = tkfont.Font(family="Helvetica", size=42, weight="bold")
        self.menu_font = tkfont.Font(family="Helvetica", size=20)
        self.subtitle_font = tkfont.Font(family="Helvetica", size=16, slant="italic")
        
        # Add shadow effect settings
        self.shadow_color = self.current_theme['shadow']
        self.shadow_offset = 3
        
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
        
        # Create main menu frame
        self.main_menu = self.create_main_menu()
        self.show_frame(self.main_menu)
        
        # Start color animation after everything is initialized
        self.animate_colors()

    def animate_colors(self):
        if not self.dark_mode:  # Only animate colors in light mode
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
        else:
            self.root.configure(bg=self.current_theme['bg'])
            if self.current_frame:
                self.update_theme_colors(self.current_frame)
        
        # Always schedule next frame
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

        # Add dark mode toggle button in top-right corner
        toggle_frame = tk.Frame(scrollable_frame)
        toggle_frame.pack(anchor='ne', padx=20, pady=10)
        
        self.dark_mode_button = tk.Button(
            toggle_frame,
            text="☾" if not self.dark_mode else "☼",
            font=self.menu_font,
            fg=self.current_theme['button_fg'],
            cursor='hand2',
            relief='flat',
            borderwidth=0,
            command=self.toggle_dark_mode
        )
        self.dark_mode_button.pack()
        
        # Title with subtle shadow effect
        title_frame = tk.Frame(scrollable_frame)
        title_frame.pack(pady=(40, 5))
        
        shadow_title = tk.Label(
            title_frame,
            text="Fun Projects",
            font=self.title_font,
            fg=self.shadow_color
        )
        shadow_title.place(x=self.shadow_offset, y=self.shadow_offset)
        
        title = tk.Label(
            title_frame,
            text="Fun Projects",
            font=self.title_font
        )
        title.pack()
        
        # Add subtitle
        subtitle = tk.Label(
            scrollable_frame,
            text="Choose your entertainment!",
            font=self.subtitle_font,
            fg=self.current_theme['subtitle_fg']
        )
        subtitle.pack(pady=(0, 30))
        
        # Update Random button styling
        random_button = tk.Button(
            scrollable_frame,
            text="Random Project",
            font=self.menu_font,
            fg=self.current_theme['button_fg'],
            cursor='hand2',
            relief='solid',  # Changed from flat to solid
            borderwidth=1,   # Added borderwidth
            activeforeground=self.current_theme['button_fg'],
            width=15,
            height=1,
            command=self.show_random_project
        )
        random_button.pack(pady=(0, 30))
        
        # Update project buttons styling
        for item in self.menu_items.keys():
            button_frame = tk.Frame(scrollable_frame)
            button_frame.pack(fill='x', pady=self.button_padding, padx=50)
            
            menu_button = tk.Button(
                button_frame,
                text=item,
                font=self.menu_font,
                fg=self.current_theme['fg'],
                cursor='hand2',
                relief='solid',  # Changed from flat to solid
                borderwidth=1,   # Added borderwidth
                activeforeground=self.current_theme['button_fg'],
                width=25,
                height=1,
                command=lambda name=item: self.show_project_page(name)
            )
            menu_button.pack(expand=True, pady=5, ipady=8)
            
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
            fg=self.current_theme['fg'],
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
            fg=self.current_theme['fg']
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
                fg=self.current_theme['fg']
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
        button.configure(
            fg=self.current_theme['button_fg'],
            relief='solid',  # Keep solid relief
            borderwidth=2    # Increase border width on hover
        )
        # Create hover effect with lighter/darker background
        bg_color = button.master.cget('bg')
        rgb = tuple(button.master.winfo_rgb(bg_color))
        if self.dark_mode:
            new_rgb = tuple(min(65535, val + 5000) for val in rgb)
        else:
            new_rgb = tuple(min(65535, val + 8000) for val in rgb)
        new_color = '#{:04x}{:04x}{:04x}'.format(*new_rgb)
        button.configure(bg=new_color)
        
    def on_leave_with_bg(self, button):
        button.configure(
            fg=self.current_theme['fg'],
            relief='solid',    # Keep solid relief
            borderwidth=1      # Return to normal border width
        )
        bg_color = button.master.cget('bg')
        button.configure(bg=bg_color)

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

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.current_theme = self.dark_theme if self.dark_mode else self.light_theme
        self.shadow_color = self.current_theme['shadow']
        
        # Update button text with simpler Unicode symbols
        self.dark_mode_button.configure(
            text="☼" if self.dark_mode else "☾",
            fg=self.current_theme['button_fg']
        )
        
        # Update colors for all widgets
        self.update_theme_colors(self.current_frame)
    
    def update_theme_colors(self, widget):
        if not widget:
            return
            
        if isinstance(widget, tk.Button):
            is_random = 'Random' in widget.cget('text')
            widget.configure(
                fg=self.current_theme['button_fg'] if is_random else self.current_theme['fg'],
                bg=self.current_theme['bg'],
                highlightbackground=self.current_theme['border'],  # Add border color
                highlightcolor=self.current_theme['border']       # Add border color
            )
        elif isinstance(widget, tk.Label):
            if widget.cget('text') == "Choose your entertainment!":
                widget.configure(fg=self.current_theme['subtitle_fg'])
            else:
                widget.configure(fg=self.current_theme['fg'])
            widget.configure(bg=self.current_theme['bg'])
        else:
            widget.configure(bg=self.current_theme['bg'])
        
        # Update all child widgets
        for child in widget.winfo_children():
            self.update_theme_colors(child)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()
