class AD():
    """DEFINITION
    """

    def __init__(self):
        print("""
        Welcome to Bitter Dispute! America's favorite automatically
        differentiating gameshow. Let's get started.
        """)

        variable_count = int(input(
        "How many variables are in your formula? Your limit is 26. >> "))

        count = 0
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","z","y","x"] # Re-ordered to use x and y more often

        print(f"Great, we'll use {variable_count} variables.")

        variable_dict = {}
        while count < variable_count:
            print(f"Please enter a value for variable number {count+1}.")
            variable_key = alphabet[-variable_count+count]
            variable_value = int(input(f"{variable_key} = "))
            vars()[variable_key] = variable_value
            variable_dict[variable_key] = variable_value # Should I save Node object?
            count += 1
        print("Thank you, we recorded these values:")
        for keys, values in variable_dict.items():
            print(f"{keys} = {values}")

        print("Lastly, what formula would you like to derive? Please use the variables just listed.")
        formula_str = input() # Saves string of formula
        formula = eval(formula_str)
        # If a user enters "x", it will evaluate as Node(variable_value)
        # Expectation is entering formula with variables runs it
        # Ex: >>> eval(input())
        # 3+4*x
        # 19

        # Save final outputs to class object
        self.val = formula
        #self.der = formula.der
        self.formula = formula_str

        print(f"The final value is {self.val}. Thanks for playing!")

    def __str__(self):
        """
        Defines what is printed when class is printed
        """
        return f"Formula used is {self.formula}"


class Node():
    """DEFINITION
    """

    def __init__(self, value, derivative=0):
        """
        Sets the value of the function and derivative
        """
        self.val = value
        self.der = derivative # 0 at start given value is inputted as int

    # BASIC OPERATIONS
    def __add__():
        """
        This changes what happens when you use '+'
        """
        #print("-----Addition Operation-----") # Uncomment for detailed logs
        try:
            #print("Trying object addition") # Uncomment for detailed logs
            value = self.val + other.val
            # derivative = TODO
            #print("Addition successful") # Uncomment for detailed logs
            return Node(value)
        except AttributeError as AE:
            #print(AE) # Uncomment for detailed logs
            #print("Converting to object") # Uncomment for detailed logs
            other_toy = Node(other)
            return self.__add__(other_toy)
        except TypeError as TE:
            print("-----------------------------------------------------")
            #print(TE) # Uncomment for detailed logs
            print("Please enter an integer or decimal into the equation.")
            print("-----------------------------------------------------")

    def __sub__():
        """
        This changes what happens when you use '-'
        """
        #print("-----Subtraction Operation-----") # Uncomment for detailed logs
        try:
            #print("Trying object subtraction") # Uncomment for detailed logs
            value = self.val - other.val
            # derivative = TODO
            #print("Subtraction successful") # Uncomment for detailed logs
            return Node(value)
        except AttributeError as AE:
            #print(AE) # Uncomment for detailed logs
            #print("Converting to object") # Uncomment for detailed logs
            other_toy = Node(other)
            return self.__sub__(other_toy)
        except TypeError as TE:
            print("-----------------------------------------------------")
            #print(TE) # Uncomment for detailed logs
            print("Please enter an integer or decimal into the equation.")
            print("-----------------------------------------------------")

    def __mul__():
        """
        This changes what happens when you use '*'
        """
        #print("-----Multiplication Operation-----") # Uncomment for detailed logs
        try:
            #print("Trying object multiplication") # Uncomment for detailed logs
            value = self.val * other.val
            # derivative = # TODO Finish derivative calculations
            #print("Multiplication successful") # Uncomment for detailed logs
            return Node(value, derivative)
        except AttributeError as AE:
            #print(AE) # Uncomment for detailed logs
            #print("Converting to object") # Uncomment for detailed logs
            other_toy = Node(other)
            return self.__mul__(other_toy)
        except TypeError as TE:
            print("-----------------------------------------------------")
            #print(TE) # Uncomment for detailed logs
            print("Please enter an integer or decimal into the equation.")
            print("-----------------------------------------------------")

    def __div__():
        """
        This changes what happens when you use '/'
        """
        #print("-----Division Operation-----") # Uncomment for detailed logs
        try:
            #print("Trying object division") # Uncomment for detailed logs
            value = self.val / other.val
            # derivative = # TODO Finish derivative calculations
            #print("Division successful") # Uncomment for detailed logs
            return Node(value, derivative)
        except AttributeError as AE:
            #print(AE) # Uncomment for detailed logs
            #print("Converting to object") # Uncomment for detailed logs
            other_toy = Node(other)
            return self.__div__(other_toy)
        except TypeError as TE:
            print("-----------------------------------------------------")
            #print(TE) # Uncomment for detailed logs
            print("Please enter an integer or decimal into the equation.")
            print("-----------------------------------------------------")

    def __pow__():
        """
        This changes what happens when you use '**'
        """
        #print("-----Power Operation-----") # Uncomment for detailed logs
        try:
            #print("Trying object power") # Uncomment for detailed logs
            value = self.val ** other.val
            # derivative = # TODO Finish derivative calculations
            #print("Power successful") # Uncomment for detailed logs
            return Node(value, derivative)
        except AttributeError as AE:
            #print(AE) # Uncomment for detailed logs
            #print("Converting to object") # Uncomment for detailed logs
            other_toy = Node(other)
            return self.__pow__(other_toy)
        except TypeError as TE:
            print("-----------------------------------------------------")
            #print(TE) # Uncomment for detailed logs
            print("Please enter an integer or decimal into the equation.")
            print("-----------------------------------------------------")

    # REVERSE OPERATIONS
    def __radd__(self, x):
        """
        Called if left parameter does not support __add__
        and parameters are of different types
        """
        return self.__add__(x)

    def __rmul__(self, x):
        """
        Called if left parameter does not support __mul__
        and parameters are of different types
        """
        return self.__mul__(x)

    def __rsub__(self, x):
        """
        Called if left parameter does not support __sub__
        and parameters are of different types
        """
        return self.__sub__(x)

    def __rdiv__(self, x):
        # TODO IS THIS A THING?
        return self.__mul__(1/x)

    def __rpow__(self, x):
        """
        Called if left parameter does not support __pow__
        and parameters are of different types
        """
        return self.__pow__(x)

    # UNARY OPERATIONS
    def __neg__(self):
        """
        This changes what happens when you use '-' in front of a value
        instead of as an operation.
        """
        return Node(-self.val, -self.der)

    def __pos__(self):
        """
        This changes what happens when you use '+' in front of a value
        instead of as an operation.
        """
        return Node(+self.val, +self.der)













# Test code for handling saved state and direct entry at a later time

   #      if len(args) > 1: # Formula and values are entered at start
   #         print("Variable count:", len(args))
   #         self.formula = args[0]
   #         self.values = args[1:]    # Starts as Tuple
   #         self.variable_count = len(args[1:])
   #         self.derivative = 0
   #
   #     elif len(args) == 1: # Only the formula is entered
   #         print("Formula is ", args[0])
   #         self.formula = args[0]
   #
   #     else: # No formula or values are entered - full walkthrough
   #         print("Initiate derivation")
   #         print("Please enter a formula you would like to derive.")
   #         self.formula = input("Write formula: ")
   #         print(f"We will derive with formula {self.formula}")
   #         print("How many values would you like to enter?")
   #         self.variable_count = input("Enter variable count: ")
   #
   #
   # def new_values(self, *values: float):
   #     """To be used with an existing formula
   #     """
   #     pass
   #
   # def __neg():
   #      Necessary for unary operations
   #     pass
