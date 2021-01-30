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
                self.display.text = str(float(calculation)*-1)
            except Exception:
                self.display.text = "Syntax Error"

    def decimal(self, calculation):
        if "." not in calculation:
            try:
                self.display.text = str(calculation+".")
            except Exception:
                self.display.text = "Syntax Error"


# Creating App class
class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

    # creating object and running it


calcApp = CalculatorApp()
calcApp.run() 