import numpy as np
# todoteam should we be importing elementary_functions here?

class Variable():
    """The Variable() class defines the base storage for an initial value and
    derivative while enabling the automatic differentiation of any formula
    through custom defined operations. It is the core class enabling automatic
    differentiation through any formula.

    todo update this
    """

    def __init__(self, name: str, value, derivative=1, second_derivative=0):
        self.name = name # todoteam does this get confusing if you've saved 'x' to 'a'. Can we auto-handle this?
        self.val = value
        if type(derivative) == dict:
            self.der = derivative
        else:
            self.der = {name: derivative}
        if type(derivative) == dict:
            self.der2 = second_derivative
        else:
            self.der2 = {name: second_derivative}
        self.partials = [name]

    def __str__(self):
        return f"{self.val}" # todo update

    def __add__(self, other):
        """
        This changes what happens when you use '+'
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29%2Bg%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29%2Bg%28x%29
        """
        self.partials = set(list(self.der.keys()) + list(self.der.keys()))
        temp_der = {}
        temp_der2 = {}
        try:
            temp_val = self.val + other.val

            for variable in self.partials:
                temp_der[variable] = self.der.get(variable, 0) + other.der.get(variable, 0)
                temp_der2[variable] = self.der2.get(variable, 0) + other.der2.get(variable, 0)

            return Variable(self.name, temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val + float(other)

                for variable in self.partials:
                    temp_der[variable] = self.der.get(variable, 0) + 0
                    temp_der2[variable] = self.der2.get(variable, 0) + 0
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
                print("Invalid input type: ", other)

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
        self.partials = set(list(self.der.keys()) + list(self.der.keys()))
        temp_der = {}
        temp_der2 = {}
        try:
            temp_val = self.val - other.val

            for variable in self.partials:
                temp_der[variable] = self.der.get(variable, 0) - other.der.get(variable, 0)
                temp_der2[variable] = self.der2.get(variable, 0) - other.der2.get(variable, 0)

            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val - float(other)

                for variable in self.partials:
                    temp_der[variable] = self.der.get(variable, 0) - 0
                    temp_der2[variable] = self.der2.get(variable, 0) - 0
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
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
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val * float(other)
                temp_der = self.der * float(other)
                temp_der2 = self.der2 * float(other)
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
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
            temp_der = (other.val * self.der - self.val * other.der) / (other.val**2)
            temp_der2 = ( (other.val**2) * self.der2 - other.val * (2 * self.der * other.der + self.val * other.der2) + 2 * self.val * (other.der**2) ) / (other.val ** 3)
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                temp_val = self.val / float(other)
                temp_der = self.der / float(other)
                temp_der2 = self.der2 / float(other)
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
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
        try:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29**g%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29**g%28x%29
        except AttributeError: (Same if you use 3 instead of y)
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29**y
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29**y
        """
        try:
            temp_val = self.val ** other.val
            temp_der = (self.val ** (other.val - 1)) * (other.val * self.der + self.val * np.log(self.val) * other.der)
            temp_der2 = (self.val ** other.val) * ( other.val * self.der / self.val + np.log(self.val) * other.der )**2 + \
                        (self.val ** other.val) * ( other.val * self.der2 / self.val + 2 * self.der * other.der / self.val - \
                            other.val * (self.der**2) / (self.val**2) + np.log(self.val) * other.der2 )
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #power rule
                n = float(other)
                temp_val = self.val**(n)
                temp_der = n * self.val**(n-1) * self.der
                temp_der2 = n * self.val**(n-2) * (self.val * self.der2 + (n-1) * (self.der**2))
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
                print("Invalid input type: ", other)

    def __rpow__(self, other):
        """
        Called if left parameter does not support __pow__
        and parameters are of different types
        Reference:
        try:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+g%28x%29**f%28x%29
            temp_der2:https://www.wolframalpha.com/input/?i=second+derivative+of+g%28x%29**f%28x%29
        except:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+y**f%28x%29
            temp_der2:https://www.wolframalpha.com/input/?i=second+derivative+of+y**f%28x%29
        """
        try:
            temp_val = other.val ** self.val
            temp_der = (other.val ** (self.val - 1)) * ( other.val * self.der * np.log(other.val) + self.val * other.der )
            temp_der2 = (other.val ** self.val) * ( self.der * np.log(other.val) + self.val * other.der / other.val)**2 + \
                        (other.val ** self.val) * ( self.der2 * np.log(other.val) + 2 * self.der * other.der / other.val + \
                        self.val * other.der2 / other.val - self.val * (other.der**2) / (other.val**2) )
            return Variable(temp_val, temp_der, temp_der2)
        except AttributeError:
            try:
                #exponential rule
                n = float(other)
                temp_val = (n)**self.val
                temp_der = np.log(n) * (n ** self.val) * self.der
                temp_der2 = np.log(n) * (n ** self.val) * ( self.der2 + np.log(n) * (self.der**2) )
                return Variable(temp_val, temp_der, temp_der2)
            except ValueError:
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

    # Comparison Methods
    def __eq__(self, other):
        """Equal Method for Variable Class"""
        try:
            return (self.val == other.val)
        except AttributeError:
            return (self.val == other)

    def __ne__(self, other):
        """Not Equal Method for Variable Class"""
        try:
            return not (self.val == other.val)
        except AttributeError:
            return not (self.val == other)

    def __lt__(self, other):
        """Less Than Method for Variable Class"""
        try:
            return  (self.val < other.val)
        except AttributeError:
            return  (self.val < other)

    def __le__(self, other):
        """Less Than or Equal Method for Variable Class"""
        try:
            return  (self.val <= other.val)
        except AttributeError:
            return  (self.val <= other)

    def __gt__(self, other):
        """Greater Than Method for Variable Class"""
        try:
            return  (self.val > other.val)
        except AttributeError:
            return  (self.val > other)

    def __ge__(self, other):
        """Greater Than or Equal Method for Variable Class"""
        try:
            return  (self.val >= other.val)
        except AttributeError:
            return  (self.val >= other)
