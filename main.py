# Program to create a calculator  

import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
# Setting size to resizable
Config.set('graphics', 'resizable', 1)


# Creating Layout class 
class CalcGridLayout(GridLayout):

    # Function called when equals is pressed 
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Syntax Error"

    def negate(self, calculation):
        if calculation:
            try:
                if calculation == "0":
                    self.display.text = calculation
                elif "." in calculation:
                    self.display.text = str(float(calculation)*-1)
                else:
                    self.display.text = str(int(calculation)*-1)
            except Exception:
                self.display.text = "Syntax Error"

    def decimal(self, calculation):
        if "." not in calculation:
            try:
                self.display.text = str(calculation+".")
            except Exception:
                self.display.text = "Syntax Error"

    # def __init__(self):
    #     self.List = []

    def numFunc(self, entry, number):
        try:
            self.display.text = str(entry+number)
        except Exception:
            self.display.text = "Syntax Error"


    List = []
    def addToList(self, entry, char):
        try:
            if len(self.List) > 0:
                if self.List[ -1 ] == "=":
                    self.List = []
                    entry=""
            self.List.append(char)
            # print(self.List)

            signlist= ["-" , "+", "*", "/" , "%"]
            if entry == "":
                if char in signlist:
                    entry = "0"

            if entry == "0":
                if char == "0":
                    self.display.text= "0"
                    return None

            numList = ["1", "2" , "3", "4" , "5" , "6" , "7" , "8" , "9" , "0", "-" , "+", "*", "/" , "%"]
            if char in numList:
                self.numFunc(entry,char)
            elif char == ".":
                self.decimal(entry)
            elif char == "=":
                self.calculate(entry)
            elif char == "+/-":
                self.negate(entry)
            elif char == "C" or char == "CE":
                entry= ""
                self.display.text = ""
                self.List=[]
        except Exception:
            self.display.text = "Syntax Error"




# Creating App class
class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

    # creating object and running it


calcApp = CalculatorApp()
calcApp.run() 