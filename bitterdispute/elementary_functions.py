from bitterdispute.variable import Variable
import numpy as np
import math

def sin(x):
    '''Returns Variable obj of sin(x)
    '''
    try:
        new_x = Variable(name=x.name, value=np.sin(x.val), derivative=x.der)

        for key in x.der:
            new_x.der[key] = x.der.get(key)*np.cos(x.val)
        return new_x
    except AttributeError: # constant
        return np.sin(x)


def cos(x): #--> -sin
    """Defines what happens when cosine operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    """
    try:
        new_x = Variable(name = x.name, value = np.cos(x.val), derivative = x.der)
        for key in x.der:
            x.der[key] = x.der.get(key)*(-np.sin(x.val))
        return new_x
    except AttributeError:
        return np.cos(x)


def tan(x): #--> 1/cos^2(x)
    """Defines what happens when tangent operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    """
    try:
        new_x = Variable(name = x.name, value = np.tan(x.val), derivative = x.der)
        for key in x.der:
            x.der[key] = x.der.get(key)*(1 / (np.cos(x.val) ** 2))
        return new_x
    except AttributeError:
        return np.tan(x)


def sqrt(x):
    """Defines what happens when square root operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    """
    try:
        #Ensure input domain valid
        if x.val < 0:
            raise ValueError('Cannot evaluate the square root of a negative number')
        x_new = Variable(name = x.name, value = np.sqrt(x.val), derivative = x.der)
        for key in x.der:
            x.der[key] = x.der.get(key)*(1/(2*np.sqrt(x.val)))
        return x_new
    except AttributeError:
        return np.sqrt(x)


def log(x, base=math.e):
    """Defines what happens when log operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    """
    try:
        #Ensure input domain valid
        if x.val <=0:
            raise ValueError('Cannot evaluate the log of a non-positive number')
        new_x = Variable(name = x.name, value = math.log(x.val, base), derivative = x.der)
        for key in x.der:
            x.der[key] = x.der.get(key)/(x.val * math.log(base))
        return new_x
    except AttributeError:
        return math.log(x, base)


def exp(x):
    '''Returns Variable obj of exp(x)
    '''
    try:
        new_x = Variable(name=x.name, value = np.exp(x.val), derivative = x.der)
        for key in x.der:
            new_x.der[key] = x.der.get(key)*new_x.val
        return new_x
    except AttributeError: # constant
        return np.exp(x)


def arcsin(x):
    """Returns Variable obj of arcsin(x)
    """
    try:
        if x.val < -1.0 or x.val > 1.0:
            raise ValueError("input of arcsin should within (-1, 1)")

        new_x = Variable(name=x.name, value = np.arcsin(x.val), derivative = x.der)
        for key in x.der:
            new_x.der[key] = 1/np.sqrt(1 - x.val**2)*x.der.get(key)
        return new_x
    except AttributeError: # constant
        if x < -1.0 or x > 1.0:
            raise ValueError("input of arcsin should within (-1, 1)")
        return np.arcsin(x)


def arccos(x):
    """Returns Variable obj ofarccos(x)
    """
    try:
        if x.val < -1.0 or x.val > 1.0:
            raise ValueError("input of arccos should within (-1, 1)")

        new_x = Variable(name=x.name, value = np.arccos(x.val), derivative = x.der)
        for key in x.der:
            new_x.der[key] = -1/np.sqrt(1 - x.val**2)*x.der.get(key)
        return new_x
    except AttributeError: # constant
        if x < -1.0 or x > 1.0:
            raise ValueError("input of arcsin should within (-1, 1)")
        return np.arccos(x)


def arctan(x):
    """Returns Variable obj of arctan(x)
    """
    try:
        new_x = Variable(name=x.name, value = np.arctan(x.val), derivative = x.der)
        for key in x.der:
            new_x.der[key] = 1/(1+x.val**2)*x.der.get(key)
        return new_x
    except AttributeError: # constant
        return np.arctan(x)

def sinh(x):
    '''Defines what happens when hyperbolic sine operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    '''
    try:
        # Create a Variable instance
        new_x = Variable(name=x.name, value = np.sinh(x.val), derivative = x.der)
        for key in x.der:
            new_x.der[key] = x.der.get(key)*np.cosh(x.val)
        return new_x
    except AttributeError: # if x = constant
        return math.sinh(x)


def cosh(x):
    '''RDefines what happens when hyperbolic cosine operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    '''
    try:
        # Create a Variable instance
        new_x = Variable(name=x.name, value = np.cosh(x.val), derivative = x.der)
        for key in x.der:
            # quality check
            new_x.der[key] = x.der.get(key)*np.sinh(x.val)
        return new_x
    except AttributeError: # if x = constant
        return math.cosh(x)


def tanh(x):
    '''Defines what happens when hyperbolic tangent operations performed on
    a Variable() object or a constant value. Includes calculation of derivative.
    '''
    print(x)
    try:
         # Create a Variable instance
        new_x = Variable(name=x.name, value = np.tanh(x.val), derivative = x.der)
        for key in x.der:
            # quality check
            new_x.der[key] = x.der.get(key)*((1.0/np.cosh(x.val))**2)
        return new_x
    except AttributeError: # if x = constant
        return math.tanh(x)
