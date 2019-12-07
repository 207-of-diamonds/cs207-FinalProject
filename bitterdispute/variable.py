import numpy as np

class Variable():
    """The Variable() class defines the base storage for an initial value and
    derivative while enabling the automatic differentiation of any formula
    through custom defined operations. It is the core class enabling automatic
    differentiation through any formula.

    todo update this
    """

    def __init__(self, value, derivative=1, second_derivative=0, name="x"):
        self.name = name # todoteam does this get confusing if you've saved 'x' to 'a'. Should we auto-handle this?
        self.val = np.array(value)
        self.der = np.array([derivative]*len(self.val)) # todo what should derivs be if list of values entered?
        self.der2 = np.array([second_derivative]*len(self.val))

    def __str__(self):
        return f"{self.name}: {self.val}"

    def __add__(self, other):
        """
        This changes what happens when you use '+'
        """
        try:
            # todoteam how should I update variable name?
            # todo need to check for list equivalence
            # todoteam how should we handle lack of list equivalence?
            temp_val = self.val + other.val
            temp_der = self.der + other.der
            temp_der2 = self.der2 + other.der2
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val + float(other)
                temp_der = self.der + 0
                temp_der2 = self.der2 + 0
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)
                # todo should we manually specify the types that are acceptable?

    def __radd__(self, other):
        """
        Called if left parameter does not support __add__
        and parameters are of different types
        """
        # todo can I shorten this to just 'return self+other'
        try:
            temp_val = self.val + other.val
            temp_der = self.der + other.der
            temp_der2 = None
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val + float(other)
                temp_der = self.der + 0
                temp_der2 = None
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __sub__(self, other):
        """
        This changes what happens when you use '-'
        """
        try:
            temp_val = self.val - other.val
            temp_der = self.der - other.der
            temp_der2 = self.der2 - other.der2
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val - float(other)
                temp_der = self.der - 0
                temp_der2 = self.der2 - 0
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rsub__(self, other):
        """
        Called if left parameter does not support __sub__
        and parameters are of different types
        """
        try:
            temp_val = other.val - self.val
            temp_der = other.der - self.der
            temp_der2 = None
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = float(other) - self.val
                temp_der = 0 - self.der
                temp_der2 = None
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __mul__(self, other):
        """
        This changes what happens when you use '*'
        """
        try:
            temp_val = self.val * other.val
            temp_der = self.val * other.der + self.der * other.val
            temp_der2 = self.val * other.der2 + self.der2 * other.val # todo validate this
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                temp_der2 = self.der2 * float(other)
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rmul__(self, other):

        """
        Called if left parameter does not support __mul__
        and parameters are of different types
        """
        try:
            temp_val = self.val * other.val
            temp_der = self.val * other.der + self.der * other.val
            temp_der2 = self.val * other.der2 + self.der2 * other.val # todo validate this
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                temp_der2 = self.der2 * float(other)
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __truediv__(self, other):
        """
        This changes what happens when you use '/'
        """
        try:
            temp_val = self.val / other.val
            temp_der = self.val * (-1 * (other.val)**(-2)) * other.der + self.der * (other.val)**(-1)
            # failing because np.array doesn't allow negative int powers. Python acn do this 1x1 though...
            temp_der2 = self.val * (-1 * (other.val)**(-2)) * other.der2 + self.der2 * (other.val)**(-1) # todo validate this.
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val / float(other)
                temp_der = self.der / float(other)
                temp_der2 = self.der2 / float(other)
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rtruediv__(self, other):
        """
        Called if left parameter does not support __truediv__
        and parameters are of different types
        """
        try:
            temp_val = self.val / other.val
            temp_der = self.val * (-1 * (other.val)**(-2)) * other.der + self.der * (other.val)**(-1)
            temp_der2 = None
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = float(other) / self.val
                temp_der = (-1) * float(other) * self.val**(-2)*self.der
                temp_der2 = None
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __pow__(self, other):
        """
        This changes what happens when you use '**'
        """
        try:
            temp_val = self.val ** other.val
            temp_der = (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der
            temp_der2 = (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der2
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #power rule
                n = float(other)
                temp_val = self.val**(n)
                temp_der = n * self.val**(n-1) * self.der
                temp_der2 = n * self.val**(n-1) * self.der2
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rpow__(self, other):
        """
        Called if left parameter does not support __pow__
        and parameters are of different types
        """
        try:
            temp_val = other.val ** self.val
            temp_der = (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der
            temp_der2 = None
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #exponential rule
                n = float(other)
                temp_val = (n)**self.val
                temp_der = n**self.val * np.log(n) * self.der
                temp_der2 = None
                return Variable(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    # Unary Operations
    def __neg__(self):
        """
        This changes what happens when you use '-' in front of a value
        instead of as an operation.
        This can also be used to make a negative number positive. -(-1) = 1
        """
        # todoteam confirm what derivative of negative value is
        return Variable(-self.val, -self.der, -self.der2)
