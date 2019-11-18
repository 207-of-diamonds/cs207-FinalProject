from scalar import Scalar
from elementary_functions import *

class AD():
    """DEFINITION
    """

    def __init__(self):
        print("""
        Welcome to Bitter Dispute! America's favorite automatically
        differentiating gameshow. Let's get started.
        """)

        try:
            variable_count = int(input("How many variables are in your formula? Your limit is 26. >> "))
        except:
            print("Please enter an integer value.")
            variable_count = int(input("How many variables are in your formula? Your limit is 26. >> "))


        count = 0
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","z","y","x"] # Re-ordered to use x and y more often

        print(f"Great, we'll use {variable_count} variables.")

        variable_dict = {}
        while count < variable_count:
            print(f"Please enter a value for variable number {count+1}.")
            variable_key = alphabet[-variable_count+count]
            variable_value = float(input(f"{variable_key} = "))
            vars()[variable_key] = Scalar(variable_value)
            variable_dict[variable_key] = Scalar(variable_value)
            count += 1
        print("Thank you, we recorded these values:")
        for keys, values in variable_dict.items():
            print(f"{keys} = {values.val}")

        print("Lastly, what formula would you like to derive? Please use the variables just listed.")
        formula = input() # Saves string of formula
        function = eval(formula)
        # If a user enters "x", it will evaluate as Scalar(variable_value)
        # Expectation is entering formula with variables runs it
        # Ex: >>> eval(input())
        # 3+4*x
        # 19

        # Save final outputs to AD class object
        self.val = function.val
        self.der = function.der
        self.formula = formula

        print(f"The final derivative of formula {self.formula} with your chosen values is {self.der}. Thanks for playing!")

    def __str__(self):
        """
        Defines what is printed when class is printed
        """
        return f"Formula used is {self.formula}"