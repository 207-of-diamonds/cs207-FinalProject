import numpy as np

class Scalar():
    """The Scalar() class defines the base storage for an initial value and
    derivative while enabling the automatic differentiation of any formula
    through custom defined operations. It is the core class enabling automatic
    differentiation through any formula.
    """

    def __init__(self, value, derivative=1):
        self.val = value
        self.der = derivative

    def __str__(self):
        return self.val

    def __add__(self, other):
        """
        This changes what happens when you use '+'
        """
        try:
            temp_val = self.val + other.val
            temp_der = self.der + other.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val + float(other)
                temp_der = self.der + 0
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __radd__(self, other):
        """
        Called if left parameter does not support __add__
        and parameters are of different types
        """
        try:
            temp_val = self.val + other.val
            temp_der = self.der + other.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val + float(other)
                temp_der = self.der + 0
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __sub__(self, other):
        """
        This changes what happens when you use '-'
        """
        try:
            temp_val = self.val - other.val
            temp_der = self.der - other.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val - float(other)
                temp_der = self.der - 0
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __rsub__(self, other):
        """
        Called if left parameter does not support __sub__
        and parameters are of different types
        """
        try:
            temp_val = other.val - self.val
            temp_der = other.der - self.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = float(other) - self.val
                temp_der = 0 - self.der
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __mul__(self, other):
        """
        This changes what happens when you use '*'
        """
        try:
            temp_val = self.val * other.val
            temp_der = self.val * other.der + self.der * other.val
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __rmul__(self, other):

        """
        Called if left parameter does not support __mul__
        and parameters are of different types
        """
        try:
            temp_val = self.val * other.val
            temp_der = self.val * other.der + self.der * other.val
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    # TODO __div__ deprecated in Python 3.x. Should we specify this version requirement in requirements.txt?

    def __truediv__(self, other):
        """
        This changes what happens when you use '/'
        """
        try:
            temp_val = self.val / other.val
            temp_der = self.val * (-1 * (other.val)**(-2)) * other.der + self.der * (other.val)**(-1)
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = self.val / float(other)
                temp_der = self.der / float(other)
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __rtruediv__(self, other):
        """
        Called if left parameter does not support __truediv__
        and parameters are of different types
        """
        try:
            temp_val = self.val / other.val
            temp_der = self.val * (-1 * (other.val)**(-2)) * other.der + self.der * (other.val)**(-1)
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                temp_val = float(other) / self.val
                temp_der = (-1) * float(other) * self.val**(-2)*self.der
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    # TODO Implement __floordiv__

    def __pow__(self, other):
        """
        This changes what happens when you use '**'
        """
        try:
            temp_val = self.val ** other.val
            temp_der = (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                #power rule
                n = float(other)
                temp_val = self.val**(n)
                temp_der = n * self.val**(n-1) * self.der
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    def __rpow__(self, other):
        """
        Called if left parameter does not support __pow__
        and parameters are of different types
        """
        try:
            temp_val = other.val ** self.val
            temp_der = (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der
            return Scalar(temp_val, temp_der)
        except AttributeError:
            try:
                #exponential rule
                n = float(other)
                temp_val = (n)**self.val
                temp_der = n**self.val * np.log(n) * self.der
                return Scalar(temp_val, temp_der)
            except AttributeError:
                print("Invalid input : ", other)

    # UNARY OPERATIONS
    def __neg__(self):
        """
        This changes what happens when you use '-' in front of a value
        instead of as an operation.
        """
        return Scalar(-self.val, -self.der)

    # TODO Should we define or delete this?
    def __pos__(self):
        """
        This changes what happens when you use '+' in front of a value
        instead of as an operation.
        """
        return Scalar(+self.val, +self.der)
