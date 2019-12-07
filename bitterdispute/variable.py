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
        Reference:
            temp_der: https://www.wolframalpha.com/input/?i=first+derivative+of+f%28x%29%2Bg%28x%29
            temp_der2: https://www.wolframalpha.com/input/?i=second+derivative+of+f%28x%29%2Bg%28x%29
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
        return self - other

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
            # failing because np.array doesn't allow negative int powers. Python acn do this 1x1 though...
            temp_der2 = ( (other.val**2) * self.der2 - other.val * (2 * self.der * other.der + self.val * other.der2) + 2 * self.val * (other.der**2) ) / (other.val ** 3)
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
        return self / other

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
        return self ** other

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
        """Equal Method for Variable Class

        todoteam what to do in this case
        >>> np.array([1,2,3])==np.array([1,2,3])
array([ True,  True,  True])
>>> np.array([1,2,3])==np.array([1,3,3])
array([ True, False,  True])
        """
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
