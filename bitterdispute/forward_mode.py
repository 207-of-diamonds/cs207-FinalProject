from bitterdispute.variable import Variable
from bitterdispute.elementary_functions import *

class AD():
    """The AD() class creates a step-by-step walkthrough for users who wish to
    automatically differentiate a chosen formula and values. A user can save
    the output values of the formula and the derivative of the formula to a
    variable in Python using something like x = AD() for later reference.

    todo update to handle vector of functions
    """

    def __init__(self):
        self.guide()

    def guide(self):
        """todo
        """
        print("""
        Welcome to Bitter Dispute! America's favorite automatically
        differentiating gameshow. Let's get started.
        """)
        try:
            variable_count = int(input("How many variables are in your formula(s)? The limit is 26. >> "))
        except:
            print("Please enter an integer value.")
            variable_count = int(input("How many variables are in your formula(s)? the limit is 26. >> "))


        count = 0
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","z","y","x"] # Re-ordered to use x and y more often

        print(f"Great, we'll use {variable_count} variables.")

        variable_dict = {}
        while count < variable_count:
            print(f"Please enter a value for variable number {count+1}.")
            variable_key = alphabet[-variable_count+count]
            variable_value = float(input(f"{variable_key} = "))
            globals()[variable_key] = Variable(variable_key, variable_value)
            variable_dict[variable_key] = Variable(variable_key, variable_value)
            count += 1
        print("Thank you, we recorded these values:")
        for keys, values in variable_dict.items():
            print(f"{keys} = {values}")#.val

        print("""Lastly, what formulas would you like to derive? Please use the variables just listed.
        You may enter as many formulas as you'd like, either writing them separated by commas or copying a list.""")
        formulas = input()
        # If a list of formulas is entered
        if formulas[0] == '[':
            formulas = formulas[1:-1].split(',') # Saves string of formula minus first/last spots representing []
        # If multiple formulas are manually written
        else:
            formulas = formulas.split(',') # Saves string of formula split on comma to make list
        functions = [eval(formula) for formula in formulas]

        # Save final outputs to AD class object
        inputs = {}
        for key, value in variable_dict.items():
            inputs[key] = value.val
        self.inputs = inputs
        self.outputs = [function.val for function in functions]
        self.derivatives = [function.der for function in functions]
        self.second_derivatives = [function.der2 for function in functions]
        self.formulas = formulas

        if len(formulas) == 1:
            print(f"The final derivative of formula {self.formulas} with your chosen values is {self.derivatives}. Thanks for playing!")
        else:
            print(f"The final derivatives of formulas {self.formulas} with your chosen values are {self.derivatives}. Thanks for playing!")


    def __str__(self):
        """
        Defines what is printed when class is printed
        """
        return f"""
        Formula(s) saved: {self.formulas},
        Value(s) used: {self.inputs},
        Derivatives found: {self.derivatives}
        """

    def new_values(self):
        """
        Allows you to pass in new values with saved formulas
        todo
        """
        variable_dict = {}
        for variable_key in self.inputs.keys():
            print(f"Please enter new value for {variable_key}")
            variable_value = float(input(f"{variable_key} = "))
            globals()[variable_key] = Variable(variable_key, variable_value)
            variable_dict[variable_key] = Variable(variable_key, variable_value)
        print("Thank you, we recorded these values:")
        for key, value in variable_dict.items():
            print(f"{key} = {value}")

        functions = [eval(formula) for formula in self.formulas]

        inputs = {}
        for key, value in variable_dict.items():
            inputs[key] = value.val
        self.inputs = inputs
        self.outputs = [function.val for function in functions]
        self.derivatives = [function.der for function in functions]
        self.second_derivatives = [function.der2 for function in functions]

        if len(self.formulas) == 1:
            print(f"The final derivative of formula {self.formulas} with your chosen values is {self.derivatives}. Thanks for playing!")
        else:
            print(f"The final derivatives of formulas {self.formulas} with your chosen values are {self.derivatives}. Thanks for playing!")

    def new_formulas(self):
        """
        Allows you to pass in new formulas for saved values
        todo
        """
        for variable_key, variable_value in self.inputs.items():
            globals()[variable_key] = Variable(variable_key, variable_value)


        print("""What new formulas would you like to derive? Please use the same saved variables.
        You may enter as many formulas as you'd like, either writing them separated by commas or copying a list.""")
        formulas = input()
        # If a list of formulas is entered
        if formulas[0] == '[':
            formulas = formulas[1:-1].split(',') # Saves string of formula minus first/last spots representing []
        # If multiple formulas are manually written
        else:
            formulas = formulas.split(',') # Saves string of formula split on comma to make list

        functions = [eval(formula) for formula in formulas]

        # Save final outputs to AD class object
        self.outputs = [function.val for function in functions]
        self.derivatives = [function.der for function in functions]
        self.second_derivatives = [function.der2 for function in functions]
        self.formulas = formulas

        if len(formulas) == 1:
            print(f"The final derivative of formula {self.formulas} with your chosen values is {self.derivatives}. Thanks for playing!")
        else:
            print(f"The final derivatives of formulas {self.formulas} with your chosen values are {self.derivatives}. Thanks for playing!")
