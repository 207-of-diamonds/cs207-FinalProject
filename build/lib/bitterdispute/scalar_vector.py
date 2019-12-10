import numpy as np

class Scalar():

    def __init__(self, value, der=1, name='x'):
        self.val = {name: value} # TODO Should edit this
        self.der = {name: der}
        self.name = name

    def __str__(self):
        return self.val

    def __add__(self, other):
        try:
            temp_val = self.val[self.name] + other.val[self.name]
            temp_der = self.der[self.name]+other.der[other.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = self.val[self.name] + float(other)
                temp_der = self.der[self.name] + 0
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __radd__(self, other):
        try:
            temp_val = self.val[self.name] + other.val[self.name]
            temp_der = self.der[self.name]+other.der[other.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = self.val[self.name] + float(other)
                temp_der = self.der[self.name] + 0
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __sub__(self, other):
        try:
            temp_val = self.val[self.name] - other.val[self.name]
            temp_der = self.der[self.name]-other.der[other.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = self.val[self.name] - float(other)
                temp_der = self.der[self.name] - 0
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __rsub__(self, other):
        try:
            temp_val = other.val[self.name] - self.val[self.name]
            temp_der = other.der[self.name] - self.der[self.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = float(other)-self.val[self.name]
                temp_der = 0 - self.der[self.name]
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __mul__(self, other):
        try:
            temp_val = self.val[self.name] * other.val[self.name]
            temp_der = self.val[self.name] * other.der[self.name] + self.der[self.name] * other.val[self.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = self.val[self.name] * float(other)
                temp_der = self.der[self.name] * float(other)
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __rmul__(self, other):
         try:
            temp_val = self.val[self.name] * other.val[self.name]
            temp_der = self.val[self.name] * other.der[self.name] + self.der[self.name] * other.val[self.name]
            return Scalar(temp_val, temp_der, name=self.name)
         except AttributeError:
            try:
                temp_val = self.val[self.name] * float(other)
                temp_der = self.der[self.name] * float(other)
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __truediv__(self, other):
        try:
            temp_val = self.val[self.name]/other.val[self.name]
            temp_der = self.val[self.name] * (-1*(other.val[self.name])**(-2))*other.der[self.name] + self.der[self.name] * (other.val[self.name])**(-1)
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = self.val[self.name] / float(other)
                temp_der = self.der[self.name] / float(other)
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __rtruediv__(self, other):
        try:
            temp_val = self.val[self.name]/other.val[self.name]
            temp_der = self.val[self.name] * (-1*(other.val[self.name])**(-2))*other.der[self.name] + self.der[self.name] * (other.val[self.name])**(-1)
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                temp_val = float(other)/self.val[self.name]
                temp_der = (-1)*float(other)*self.val[self.name]**(-2)*self.der[self.name]
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __pow__(self, other):
        try:
            temp_val = self.val[self.name] ** other.val[self.name]
            temp_der = (self.val[self.name] ** other.val[self.name]) * (np.log(self.val[self.name]) + other.val[self.name]/self.val[self.name]) * self.der[self.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                #power rule
                n = float(other)
                temp_val = self.val[self.name]**(n)
                temp_der = n*self.val[self.name]**(n-1)*self.der[self.name]
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)

    def __rpow__(self, other):
        try:
            temp_val = other.val[self.name] ** self.val[self.name]
            temp_der = (self.val[self.name] ** other.val[self.name]) * (np.log(self.val[self.name]) + other.val[self.name]/self.val[self.name]) * self.der[self.name]
            return Scalar(temp_val, temp_der, name=self.name)
        except AttributeError:
            try:
                #exponential rule
                n = float(other)
                temp_val = (n)**self.val[self.name]
                temp_der = n**self.val[self.name]*np.log(n)*self.der[self.name]
                return Scalar(temp_val, temp_der, name=self.name)
            except AttributeError:
                print("Invalid input : ", other)
