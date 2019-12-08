import numpy as np
import math
from bitterdispute.scalar import Scalar

#trig
def sin(x): #--> cos
    """Defines what happens when sine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.sin(x.val)
        derivative = np.cos(x.val) * x.der
        return Scalar(value, derivative)
    except AttributeError: # constant
        return np.sin(x)

def cos(x): #--> -sin
    """Defines what happens when cosine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.cos(x.val)
        derivative = -np.sin(x.val) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return np.cos(x)

def tan(x): #--> 1/cos^2(x)
    """Defines what happens when tangent operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.tan(x.val)
        derivative = (1 / (np.cos(x.val) ** 2)) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return np.tan(x)

def arcsin(x): #--> 1/np.sqrt(1-x^2)
    """Defines what happens when inverse sine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    # if x.val < -1.0 or x.val > 1.0:
    #     print('here')
    #     raise ValueError("input of arcsin should within (-1, 1)")
    # else:
    try:
        if x.val < -1.0 or x.val > 1.0:
            raise ValueError("input of arcsin should within (-1, 1)")
        else:
            value = np.arcsin(x.val)
            derivative = (1 / np.sqrt(1 - x.val ** 2)) * x.der
            return Scalar(value, derivative)
    except AttributeError:
        if x < -1.0 or x > 1.0:
            raise ValueError("input of arcsin should within (-1, 1)")
        return np.arcsin(x)

def arccos(x):#--> -1/np.sqrt(1-x^2)
    """Defines what happens when inverse cosine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        if x.val < -1.0 or x.val > 1.0:
            raise ValueError("input of arccos should within (-1, 1)")
        else:
            value = np.arccos(x.val)
            derivative = (1 / -np.sqrt(1 - x.val ** 2)) * x.der
            return Scalar(value, derivative)
    except AttributeError:
        if x < -1.0 or x > 1.0:
            raise ValueError("input of arccos should within (-1, 1)")
        return np.arccos(x)

def arctan(x):#--> 1/(1+x^2)
    """Defines what happens when inverse tangent operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.arctan(x.val)
        derivative = (1 / (1 + x.val ** 2)) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return np.arctan(x)

def sinh(x):#--> cosh
    """Defines what happens when hyperbolic sine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = math.sinh(x.val)
        derivative = math.cosh(x.val) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return math.sinh(x)

def cosh(x):#--> sinh
    """Defines what happens when hyperbolic cosine operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = math.cosh(x.val)
        derivative = math.sinh(x.val) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return math.cosh(x)

def tanh(x):#--> 1 / (cosh^2)
    """Defines what happens when hyperbolic tangent operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = math.tanh(x.val)
        derivative = (1 / (cosh(x.val) ** 2)) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return math.tanh(x)

#exponential and log
def exp(x):
    """Defines what happens when exponential operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.exp(x.val)
        derivative = np.exp(x.val) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return np.exp(x)

def log(x, base=math.e):
    """Defines what happens when log operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = math.log(x.val, base)
        derivative = (1 / (x.val * math.log(base))) * x.der
        return Scalar(value, derivative)
    except AttributeError:
        return math.log(x, base)
    
def sqrt(x):
    """Defines what happens when square root operations performed on
    a Scalar() object or a constant value. Includes calculation of derivative.
    """
    try:
        value = np.sqrt(x.val)
        derivative = 1/(2*np.sqrt(x.val))
        return Scalar(value, derivative)
    except AttributeError:
        return np.sqrt(x)
