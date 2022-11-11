import tkinter
import tkinter.messagebox
import customtkinter
from UI.Plot import plot_function

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 720

    def __init__(self):
        super().__init__()

        self.title("Genetic Algorithm for finding MIN/MAX in Beale Function")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Beale Function",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Plot Function",
                                                command=self.plot_button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=25, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x11)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=2)
        self.frame_right.rowconfigure(10, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_info ============


        # ============ frame_right ============

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Choose Method:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=15, padx=15, sticky="")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_1.grid(row=1, column=2, columnspan=1, pady=15, padx=15, sticky="we")

        self.combobox_2 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_2.grid(row=2, column=2, columnspan=1, pady=15, padx=15, sticky="we")

        self.combobox_3 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_3.grid(row=3, column=2, columnspan=1, pady=15, padx=15, sticky="we")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Maximum")
        self.check_box_2.grid(row=4, column=2, pady=15, padx=15, sticky="w")

        self.entry_0 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Begin of rage -a")
        self.entry_0.grid(row=0, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Begin of rage -b")
        self.entry_1.grid(row=1, column=0, columnspan=2, rowspan=1, pady=15, padx=15, sticky="we")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Population amount")
        self.entry_2.grid(row=2, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Number of bits")
        self.entry_3.grid(row=3, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_4 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Epochs amount")
        self.entry_4.grid(row=4, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_5 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Best and tournament chromosome amount")
        self.entry_5.grid(row=5, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_6 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Elite Strategy amount")
        self.entry_6.grid(row=6, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_7 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Cross probability")
        self.entry_7.grid(row=7, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_8 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Mutation probability")
        self.entry_8.grid(row=8, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.entry_9 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Inversion probability")
        self.entry_9.grid(row=9, column=0, columnspan=2, pady=15, padx=15, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Start",
                                                border_width=2,  # <- custom border_width
                                                fg_color="grey",  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=10, column=0, columnspan=3, pady=15, padx=15, sticky="swe")

        # set default values
        self.combobox_1.set("Selection Method")
        self.combobox_2.set("Cross Method")
        self.combobox_3.set("Mutation Method")
        self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def plot_button_event(self):
        plot_function()
