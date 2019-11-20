

class Node():
    """DELETE THIS AFTER SCALAR CONFIRMED WORKS
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

"""
It should also contain the following elemental functions:
- exponential
- trig functions (sine, cosine, tangent) """

import numpy as np
from forward_mode import Node

#### MINIMUM IMPLEMENTATION REQUIREMENTS ###

# ELEMENTAL FUNCTIONS
def exp(self):
    """Exponential"""
    #print("-----Exponential Operation-----") # Uncomment for detailed logs
    try:
        #print("Trying object exponent") # Uncomment for detailed logs
        value = np.exp(self.val)
        # derivative = TODO
        #print("Exponential successful") # Uncomment for detailed logs
        return Node(value, derivative=)
    except AttributeError as AE:
        #print(AE) # Uncomment for detailed logs
        #print("Converting to object") # Uncomment for detailed logs
        new_node = Node(self)
        return exp(new_node)

def sin(self):
    """Sine"""
    #print("-----Sine Operation-----") # Uncomment for detailed logs
    try:
        #print("Trying object sine") # Uncomment for detailed logs
        value = np.sin(self.val)
        # derivative = TODO
        #print("Sine successful") # Uncomment for detailed logs
        return Node(value, derivative=)
    except AttributeError as AE:
        #print(AE) # Uncomment for detailed logs
        #print("Converting to object") # Uncomment for detailed logs
        new_node = Node(self)
        return sin(new_node)

def cos(self):
    """Cosine"""
    #print("-----Cosine Operation-----") # Uncomment for detailed logs
    try:
        #print("Trying object cosine") # Uncomment for detailed logs
        value = np.cos(self.val)
        # derivative = TODO
        #print("Cosine successful") # Uncomment for detailed logs
        return Node(value, derivative=)
    except AttributeError as AE:
        #print(AE) # Uncomment for detailed logs
        #print("Converting to object") # Uncomment for detailed logs
        new_node = Node(self)
        return cos(new_node)

def tan(self):
    """Tangent"""
    #print("-----Tangent Operation-----") # Uncomment for detailed logs
    try:
        #print("Trying object tangent") # Uncomment for detailed logs
        value = np.tan(self.val)
        # derivative = TODO
        #print("Tangent successful") # Uncomment for detailed logs
        return Node(value, derivative=)
    except AttributeError as AE:
        #print(AE) # Uncomment for detailed logs
        #print("Converting to object") # Uncomment for detailed logs
        new_node = Node(self)
        return tan(new_node)

# NON-REQUIRED ELEMENTAL FUNCTIONS
def arcsin():
    pass
def arccos():
    pass
def arctan():
    pass
def sinh():
    pass
def cosh():
    pass
def tanh():
    pass
def arcsinh():
    pass
def arccosh():
    pass
def arctanh():
    pass
def log():
    pass
def sqrt():
    pass
def sigmoid():
    pass
