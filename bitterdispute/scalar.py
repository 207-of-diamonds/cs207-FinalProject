import numpy as np

class Scalar():
    """The Scalar() class defines the base storage for an initial value and
    derivative while enabling the automatic differentiation of any formula
    through custom defined operations. It is the core class enabling automatic
    differentiation through any formula.

    todo update this
    """

    def __init__(self, value, derivative=1, second_derivative=0, name="x"):
        self.name = name # todoteam does this get confusing if you've saved 'x' to 'a'. Should we auto-handle this?
        self.val = value
        self.der = derivative
        self.der2 = second_derivative

    def __str__(self):
        return f"{self.name}: {self.val}" # todo update

    def __add__(self, other):
        """
        This changes what happens when you use '+'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29%2Bg%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29%2Bg%28x%29
        """
        try:
            # todoteam how should I update Scalar name?
            temp_val = self.val + other.val
            temp_der = self.der + other.der
            temp_der2 = self.der2 + other.der2
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val + float(other)
                temp_der = self.der + 0
                temp_der2 = self.der2 + 0
                return Scalar(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)
                # todo should we manually specify the types that are acceptable?

    def __radd__(self, other):
        """
        Called if left parameter does not support __add__
        and parameters are of different types
        """
        return self + other

    def __sub__(self, other):
        """
        This changes what happens when you use '-'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29-g%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29-g%28x%29
        """
        try:
            temp_val = self.val - other.val
            temp_der = self.der - other.der
            temp_der2 = self.der2 - other.der2
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val - float(other)
                temp_der = self.der - 0
                temp_der2 = self.der2 - 0
                return Scalar(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rsub__(self, other):
        """
        Called if left parameter does not support __sub__
        and parameters are of different types
        """
        return -self + other

    def __mul__(self, other):
        """
        This changes what happens when you use '*'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29*g%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29*g%28x%29
        """
        try:
            temp_val = self.val * other.val
            temp_der = other.val * self.der + self.val * other.der
            temp_der2 = other.val * self.der2 + 2 * self.der * other.der + self.val * other.der2
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                temp_der2 = self.der2 * float(other)
                return Scalar(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rmul__(self, other):

        """
        Called if left parameter does not support __mul__
        and parameters are of different types
        """
        return self * other

    def __truediv__(self, other):
        """
        This changes what happens when you use '/'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29%2Fg%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29%2Fg%28x%29
        """
        try:
            temp_val = self.val / other.val
            temp_der = (other.val * self.der - self.val * other.der) / (other.val**2) # todoteam confirm this swap is ok
            # old: self.val * (-1 * (other.val)**(-2)) * other.der + self.der * (other.val)**(-1)
            temp_der2 = ( (other.val**2) * self.der2 - other.val * (2 * self.der * other.der + self.val * other.der2) + 2 * self.val * (other.der**2) ) / (other.val ** 3)
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val / float(other)
                temp_der = self.der / float(other)
                temp_der2 = self.der2 / float(other)
                return Scalar(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rtruediv__(self, other):
        """
        Called if left parameter does not support __truediv__
        and parameters are of different types
        """
        return (self**-1) * other

    def __pow__(self, other):
        """
        This changes what happens when you use '**'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29**g%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29**g%28x%29
        """
        try:
            temp_val = self.val ** other.val
            temp_der = (self.val ** (other.val - 1)) * (other.val * self.der + self.val * np.log(self.val) * other.der) #todoteam confirm swap
            #old: (self.val ** other.val) * (np.log(self.val) + other.val / self.val) * self.der
            temp_der2 = (self.val ** other.val) * ( ((other.val * self.der) / self.val) + np.log(self.val) * other.der)**2 + \
                        (self.val ** other.val) * ( ((other.val * self.der2) / self.val) + ((2 * self.der * other.der) / self.val) - \
                            ((other.val * (self.der**2)) / (self.val**2)) + np.log(self.val)*other.der2 )
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #power rule
                n = float(other)
                temp_val = self.val**(n)
                temp_der = n * self.val**(n-1) * self.der
                temp_der2 = n * self.val**(n-1) * self.der2
                return Scalar(temp_val, temp_der, temp_der2)
            except AttributeError:
                print("Invalid input type: ", other)

    def __rpow__(self, other):
        """
        Called if left parameter does not support __pow__
        and parameters are of different types
        """
        try:
            temp_val = other.val ** self.val
            temp_der = (other.val ** (self.val - 1)) * (self.val * other.der + other.val * np.log(other.val) * self.der)
            temp_der2 = (other.val ** self.val) * ( ((self.val * other.der) / other.val) + np.log(other.val) * self.der)**2 + \
                        (other.val ** self.val) * ( ((self.val * other.der2) / other.val) + ((2 * other.der * self.der) / other.val) - \
                            ((self.val * (other.der**2)) / (other.val**2)) + np.log(other.val)*self.der2 )
            return Scalar(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #exponential rule
                n = float(other)
                temp_val = (n)**self.val
                temp_der = (n ** (self.val - 1)) * (self.val * 1 + n * np.log(n) * self.der)
                temp_der2 = (n ** self.val) * ( ((self.val * 1) / n) + np.log(n) * self.der)**2 + \
                            (n ** self.val) * ( ((self.val * 0) / n) + ((2 * 1 * self.der) / n) - \
                                ((self.val * (1**2)) / (n**2)) + np.log(n)*self.der2)
                # todoteam confirm swap n**self.val * np.log(n) * self.der
                return Scalar(temp_val, temp_der, temp_der2)
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
        return Scalar(-self.val, -self.der, -self.der2)

    # Comparison Methods
    def __eq__(self, other):
        """Equal Method for Scalar Class"""
        try:
            return (self.val == other.val)
        except AttributeError:
            return (self.val == other)

    def __ne__(self, other):
        """Not Equal Method for Scalar Class"""
        try:
            return not (self.val == other.val)
        except AttributeError:
            return not (self.val == other)

    def __lt__(self, other):
        """Less Than Method for Scalar Class"""
        try:
            return  (self.val < other.val)
        except AttributeError:
            return  (self.val < other)

    def __le__(self, other):
        """Less Than or Equal Method for Scalar Class"""
        try:
            return  (self.val <= other.val)
        except AttributeError:
            return  (self.val <= other)

    def __gt__(self, other):
        """Greater Than Method for Scalar Class"""
        try:
            return  (self.val > other.val)
        except AttributeError:
            return  (self.val > other)

    def __ge__(self, other):
        """Greater Than or Equal Method for Scalar Class"""
        try:
            return  (self.val >= other.val)
        except AttributeError:
            return  (self.val >= other)
