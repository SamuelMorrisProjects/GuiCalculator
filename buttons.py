from functools import partial
import tkinter as tk 
from tkinter import font
from ctypes import windll
from SettingsFile import settings

class ButtonInterface(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master, background="#0b0a10", width= 1)
        self.master:tk.Frame = master

        #Settings
        self.settings = settings["Settings"]["ButtonSettings"]
        self.display_limit= self.settings["NumberDisplayLimit"]
        self.font = self.settings["FontFamily"]
        self.button_background = self.settings["ButtonBackground"]
        self.button_foreground= self.settings["ButtonForeground"]
        self.display_background = self.settings["DisplayBackground"]
        self.display_foreground = self.settings["DisplayForeground"]



        #Fonts
        self.butn_font = font.Font(family=self.font, size=20,)
        self.display_font = font.Font(family=self.font, size=15,)

        self.display =tk.Label(self, background=self.display_background, text="", font= self.display_font, foreground= self.display_foreground)
        #Make section
        self.display.grid(row=0, column=1, pady=20, sticky="NSEW", columnspan=3)
        self.rowconfigure(0,minsize=175)
        self.compose_buttons()

    def output_to_display(self, item):
        displayed_string = self.display["text"]
        if item in (0,"+", "*","=","/") and len(displayed_string)==0:
             return
        if len(displayed_string)==self.display_limit:
                limited_nums=  displayed_string[:self.display_limit]
                self.display.config(text=limited_nums)
                return
        else:
            self.display.config(text= displayed_string+f'{item}')
            return

    def return_value_and_clear_display(self) ->str:
         """Returns a string representing the user input and clears the display"""
         val = self.display['text']
         self.display.config(text="")
         return val
    def compose_buttons(self):
        """Composes the buttons"""
        self.grid=[[1,2,3],
                   [4,5,6],
                   [7,8,9],]
        for i in range(1,4):
            self.grid_rowconfigure(i, weight=1)
            for j in range(1,4):
                self.grid_columnconfigure(j, weight=1)
                num = self.grid[i-1][j-1]
                tk.Button(self, text=f'{num}',height=5,width=10, background=self.button_background, foreground='#bacacf', font=self.butn_font, command=partial(self.output_to_display, num)).grid(row=i, column=j, sticky="NSEW",)
        self.grid_rowconfigure(4, weight=1)
        tk.Button(self, text="0", height=5, width=10, font=self.butn_font, background=self.button_background, foreground=self.button_foreground, command=partial(self.output_to_display, 0)).grid(row=4, column=2, sticky="NSEW",)
        tk.Button(self, text="clr", height=5, width=10, font=self.butn_font, background=self.button_background, foreground=self.button_foreground, command=partial( self.display.config, text="")).grid(row=4, column=3, sticky="NSEW",)
        tk.Button(self, text=".", height=5, width=10, font=self.butn_font, background=self.button_background, foreground=self.button_foreground, command=partial(self.output_to_display, ".")).grid(row=4, column=1, sticky="NSEW",)
