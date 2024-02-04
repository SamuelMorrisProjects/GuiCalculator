
##Imports 
from functools import partial
import tkinter as tk 
from tkinter import font
from ctypes import windll
from SettingsFile import settings, path_to_default_assets
from buttons import ButtonInterface
from sidebar import SideBarInterface

windll.shcore.SetProcessDpiAwareness(settings["Settings"]["Misc"]["SetDpiAwareness"])
base_x , base_y = 775, 700

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master, background="black")
        self.master = master
        self.buttons = ButtonInterface(self)
        self.side_bar = SideBarInterface(self, button_frame_obj=self.buttons)

        self.buttons.pack(expand = True, fill ='both', side='left')
        self.side_bar.pack(expand = True, fill ='both', side='left')

if __name__=="__main__":
    base = tk.Tk()
    base.iconbitmap(path_to_default_assets+"\calc.ico")
    base.geometry(f'{base_x}x{base_y}')
    base.title("Calculator")
    main_app = MainApplication(base).pack(side="top", fill="both", expand="true",)
    base.mainloop()
    
   