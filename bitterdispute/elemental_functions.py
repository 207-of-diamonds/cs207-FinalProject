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
