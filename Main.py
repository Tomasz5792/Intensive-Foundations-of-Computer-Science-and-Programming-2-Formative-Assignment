import customtkinter as ctk

# variables

# colours
colour_Green        = "#00AF41"
colour_GreenTint1   = "#49B066"
colour_GreenTint2   = "#72BD8A"
colour_GreenTint3   = "#9FCEAE"

colour_main = colour_Green
colour_menu = colour_GreenTint3

# text
text_size = 10
text_colour =  "#000000"
text_title_colour = "#FFFFFF"
text_title_font = ("Segoe UI", 20)
text_title_padding = 10



class App_Window(ctk.CTk):
    #main window class
    def __init__(self) -> None:
        """
        Initialises the app window and configures its settings.

        Returns:
            None
        """
        super().__init__()

        # Appearance and theme settings
        ctk.set_appearance_mode("light")  # "light" or "dark"  add a mode toggle
        ctk.set_default_color_theme("green")  # make defra green

        # settings
        self.title("Title")
        self.geometry("1200x600")
        self.minsize(900, 450)

        # components
        self.header = Frame(self, side = "top", colour_background = colour_main, height = 45)
        
        self.header_label = ctk.CTkLabel(self.header, 
                                        text="Add item to table app",
                                        text_color=text_title_colour,
                                        font=(text_title_font)
                                        )
        self.header_label.pack(side="left", padx=text_title_padding)

        self.body = Frame(self, side = "bottom")
        self.table = Frame(self.body, side = "left")
        self.menu = Frame(self.body, side = "right", colour_background = colour_menu, width = 300, corner_radius = 5, padding = 5)



class Frame(ctk.CTkFrame):
    def __init__(
            self, 
            parent, 
            side: str = "left", 
            colour_background: str = "transparent",
            width: int | None = None,
            height: int | None = None,
            #fill: str = "both",
            #expand: bool = True,
            corner_radius: int = 0,
            padding: int = 0,
            ) -> None:
        """
        A reusable customtkinter frame with flaxible layout and colour options.

        Args:
            parent (CTk or CTkFrame): The parent widget this frame will be placed inside.
            side (str, optional): The side of the parent to pack the frame on. Defaults to "left".
            colour_background (str, optional): The background color of the frame. Defaults to "transparent".
            width (int | None, optional): Fixed width of the frame in pixels. If set, the frame will not expand horizontally. Defaults to None.
            height (int | None, optional): Fixed height of the frame in pixels. If set, the frame will not expand vertically. Defaults to None.
            corner_radius (int, optional): Corner roundness of the frame in pixels. Defaults to 0.
            padding (int, optional): External padding (in pixels) applied equally on all sides. Defaults to 0.

        Returns:
            None
        """

        super().__init__(parent, fg_color=colour_background, corner_radius=corner_radius)

        fill = "both"
        expand = True

        # fixed size
        if width is not None or height is not None:
            expand = False
            self.pack_propagate(False)
            if width is not None:
                fill = "y"
                self.configure(width=width)
            if height is not None:
                fill = "x"
                self.configure(height=height)

        self.pack(side=side, expand = expand, fill = fill, padx=padding, pady=padding)

if __name__ == "__main__":
    app = App_Window()
    app.mainloop()
