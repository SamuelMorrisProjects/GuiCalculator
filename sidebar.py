from functools import partial
import tkinter as tk 
from tkinter import font
from ctypes import windll
import operator as op 
from SettingsFile import settings

class SideBarInterface(tk.Frame):
    def __init__(self, master, button_frame_obj):
        tk.Frame.__init__(self,master, background="white", width=100)
        self.master:tk.Frame = master

        #Settings from json file
        self.settings =settings["Settings"]["SidebarSettings"]
        self.font = self.settings["FontFamily"]
        self.sidebar_button_background = self.settings["ButtonBackground"]
        self.sidebar_button_foreground= self.settings["ButtonForeground"]
        self.display_background = self.settings["DisplayBackground"]
        self.display_foreground = self.settings["DisplayForeground"]

        #Operatators
       
        self.sidebar_buttons= ("+","(",")","-","*","/")

        self.button_frame =button_frame_obj

        self.butn_font = font.Font(family=self.font, size=25,)
        self.display_font = font.Font(family=self.font, size=25,)

        self.operation_display = tk.Label(self, background=self.display_background, text="", font= self.display_font, foreground=self.display_foreground)
        self.operation_display.grid(row=0, column=0, sticky="NSEW",)
        self.floating_point_digits= self.settings["RoundToDigits"]
        self.compose_buttons()
    def set_result(self):
        self.operation_display.config(text=f"{float(eval(self.button_frame.return_value_and_clear_display())):.{self.floating_point_digits}f}")
    def compose_buttons(self):
        """Composes the buttons"""
        self.columnconfigure(0,weight=1)
        for index,element in enumerate(self.sidebar_buttons):
            operation_button = tk.Button(self,height=5,width=20, background=self.sidebar_button_background, foreground=self.sidebar_button_foreground, font=self.butn_font, text=element, command=partial(self.button_frame.output_to_display, element))
            operation_button.grid(column=0,row=index+1, sticky="NSEW",)
            self.rowconfigure(index+1,weight=1)
        
        equal_button =tk.Button(self,height=4,width=20, background=self.sidebar_button_background, foreground=self.sidebar_button_foreground, font=self.butn_font, text='=', command=self.set_result)
        equal_button.grid(column=0,row=7, sticky="NSEW",)
        equal_button.rowconfigure(7,weight=1)

