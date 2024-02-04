from functools import partial
import tkinter as tk 
from tkinter import font
from ctypes import windll
import operator as op 
from SettingsFile import settings
def isNonOperator(char, ops=("x","+","-",'^')):
        if char not in ops:
            return True
        return False

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
        self.operations:dict = {"+":op.add, "-":op.sub,"*":op.mul, "/":op.truediv}
        self.sidebar_buttons= (list(self.operations.keys()))


        self.OrderOfOp = ('*',"/","+","-") #The precendence of each operator 

        self.button_frame =button_frame_obj

        self.butn_font = font.Font(family=self.font, size=25,)
        self.display_font = font.Font(family=self.font, size=25,)

        self.operation_display = tk.Label(self, background=self.display_background, text="", font= self.display_font, foreground=self.display_foreground)
        self.operation_display.grid(row=0, column=0, sticky="NSEW",)


        self.floating_point_digits=2 
        self.compose_buttons()
    @staticmethod
    def search(list1, key) ->int or bool:
        """Static method of the class SidebarInterface.
        Traverses a given list from the last element to the first and returns the index of
        a element that matches the given key. If it cannot find the key it returns false

        Parameters\n 
        list1: Sequence data type
        key: Anything"""
        for i in range(len(list1)-1,0, -1):
            if list1[i]==key:
                return i
        return False
    def _pemdas_calc(self, expresion:list[str]) ->float:
        """ Internal method of the class SidebarInterface. 
        Calculates the value from a given expression while following the order of operations\n
        Parameters\n 
        expresion: list[str] A more comprehesive example is below.
        ['1','+','1.9'] --> 2.9 """
        for operation in self.OrderOfOp:
            while self.search(expresion, operation):
                index = self.search(expresion, operation)
                expresion[index-1]= self.operations.get(operation)(float(expresion[index-1]), float(expresion[index+1]))
                del expresion[index+1]
                del expresion[index]
        return float(expresion[0])
    def _return_valid_expression_from_buttons(self) ->list[str]:
        """Creates a valid expression from the the user input.
        Expressions are formatted as a list cotaining values and operators
        EX. ['22', '+', '22']
        """
        value = self.button_frame.return_value_and_clear_display()
        expresion = ['']
        index =0 
        for i in range(len(value)):
            if isNonOperator(value[i], ops=tuple(self.sidebar_buttons)):
                expresion[index]+=(value[i])
            else:
                expresion.append(value[i])
                expresion.append('')
                index+=2
        return expresion
    def set_result(self):
        """Calculates the result, rounds its, and outputs it to the GUI interface."""
        output = self._pemdas_calc(self._return_valid_expression_from_buttons())
        print(output)
        self.operation_display.config(text=f"{output:.{self.floating_point_digits}f}")
    def compose_buttons(self):
        """Composes the buttons"""
        self.columnconfigure(0,weight=1)
        for index,element in enumerate(self.sidebar_buttons):
            operation_button = tk.Button(self,height=5,width=20, background=self.sidebar_button_background, foreground=self.sidebar_button_foreground, font=self.butn_font, text=element, command=partial(self.button_frame.output_to_display, element))
            operation_button.grid(column=0,row=index+1, sticky="NSEW",)
            self.rowconfigure(index+1,weight=1)
        equal_button =tk.Button(self,height=5,width=20, background=self.sidebar_button_background, foreground=self.sidebar_button_foreground, font=self.butn_font, text='=', command=self.set_result)
        equal_button.grid(column=0,row=5, sticky="NSEW",)
        equal_button.rowconfigure(5,weight=1)
