import numpy as np
import Scalar as sc # based on the file Caroline updated
import math

#trig
def sin(x): #-->cos
    try:
        val = np.sin(x.val)
        der = {var: np.cos(x.val) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError: # constant
        return np.sin(x)
def cos(x): #-->-sin
    try:
        val = np.cos(x.val)
        der = {var: -np.sin(x.val) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.cos(x)
def tan(x): #-->1/cos^2(x)
    try:
        val = np.tan(x.val)
        der = {var: (1 / (np.cos(x.val) ** 2)) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.tan(x)
def arcsin(x): #--> 1/np.sqrt(1-x^2)
    try:
        val = np.arcsin(x.val)
        der = {var: (1 / np.sqrt(1 - x.val ** 2)) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.arcsin(x)
def arccos(x):#--> -1/np.sqrt(1-x^2)
    try:
        val = np.arccos(x.val)
        der = {var: (1 / -np.sqrt(1 - x.val ** 2)) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.arccos(x)
def arctan(x):#--> 1/(1+x^2)
    try:
        val = np.arctan(x.val)
        der = {var: (1 / (1 + x.val ** 2)) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.arctan(x)
def sinh(x):#--> cosh
    try:
        val = math.sinh(x.val)
        der = {var: math.cosh(x.val) * der for var, der in x.der.items()}
        return scl.AD(x.var, val, der)
    except AttributeError:
        return math.sinh(x)
def cosh(x):#--> sinh
    try:
        val = math.cosh(x.val)
        der = {var: math.sinh(x.val) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return math.cosh(x)
def tanh(x):#--> 1 / (cosh^2)
    try:
        val = math.tanh(x.val)
        der = {var: (1 / (cosh(x.val) ** 2)) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return 1 / (cosh(x) ** 2)

#exponetial and power
def exp(x):
    try:
        val = np.exp(x.val)
        der = {var: val * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return np.exp(x)


def log(x, base=math.e):
    try:
        val = math.log(x.val, base)
        der = {var: (1 / (x.val * math.log(base))) * der for var, der in x.der.items()}
        return sc.AD(x.var, val, der)
    except AttributeError:
        return math.log(x, base)
