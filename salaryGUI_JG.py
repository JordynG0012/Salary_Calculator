"""
Program: salaryGUI_JG.py
Author:  Jordyn  7/19/2023

Salary Calculator for final Python project

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

# Class header (application name will change project to project)
class SalaryCalculator(EasyFrame):
    # Definition of our class constructor method
    def __init__(self):
        # Call to the Easy Frame constructor method
        EasyFrame.__init__(self, title = "Salary Calculator", height = 220, width = 295, background = "dodgerblue2", resizable = True)
        self.normalFont = Font(family = "Tahoma", size = 16)
        self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "navy", foreground = "white", font = Font(family = "Tahoma", size = 20))

        # Label and field for the hourly pay input
        self.addLabel(text = "Hourly Wage:", row = 2, column = 0, background = "salmon", foreground = "black")
        self.hourlyPayField = self.addFloatField(value = 0.0, row = 2, column = 1)
        self.hourlyPayField.config(background = "salmon")

        # Label and field for the hours worked input
        self.addLabel(text = "No. of Hours Worked:", row = 3, column = 0, background = "salmon", foreground = "black")
        self.hoursWorkedField = self.addFloatField(value = 0.0, row = 3, column = 1)
        self.hoursWorkedField.config(background = "salmon")

        # Label and field for displaying the earnings
        self.addLabel(text = "The employee's earnings is:", row = 5, column = 0, background = "salmon" , foreground = "black")
        self.earningsField = self.addFloatField(value = 0.0, row = 5, column = 1, width = 8, precision = 2)
        self.earningsField.config(background = "salmon")

        # The command button
        self.compute = self.addButton(text = "Compute", row = 4, column = 0, columnspan = 2, command = self.computeEarnings)
        self.compute["background"] = "navy"
        self.compute["foreground"] = "white"


    # Definition of the computeEarnings() function which is the event handling function
    def computeEarnings(self):
        try:
            hourly_pay = self.hourlyPayField.getNumber()
            hours_worked = self.hoursWorkedField.getNumber()
            earnings = hourly_pay * hours_worked
            self.earningsField.setNumber(earnings)
        except ValueError:
            self.messageBox(title = "ERROR", message = "Please enter valid numerical inputs for Hourly Pay and Hours Worked.")

# End of class body

# Global definition of the main() method
def main():
    # instantiate an object from the class into mainloop()
    SalaryCalculator().mainloop()
# Global call to main() for program entry
if __name__ == '__main__':
    main()
