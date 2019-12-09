
import pytest
import numpy as np

import bitterdispute.elementary_functions as elem
from bitterdispute.variable import Variable
from bitterdispute.optimization_newton_quasi_newton import *


tolerance = 1e-4
## Newton Method =====================
def test_newton_single():
    def funct(values):
        var = Variable(name='x', value=values)
        f = (var-5)**2
        return f
    
    val_1 = 1
    xn, _ = Newton(funct, val_1)
    assert np.isclose(xn, 5, tolerance)
    
    
def test_newton_vector():
    def funct_vect(values):
        var1 = Variable(name='x',value=values[0])
        var2 = Variable(name='y',value=values[1])
        f = (1.-var1)**2. + (var2-var1*var1)**2.

        return f
    
    val_1 = 0.1
    val_2 = 0.2
    xn, _ = Newton(funct_vect, x0=np.array([val_1, val_2]))
    
    
    assert np.isclose(np.mean(xn), 1, tolerance)

## QuasiNewton Method ================
def test_quasinewton_single():
    def funct(values):
        var = Variable(name='x', value=values)
        f = (var-5)**2
        return f
    
    val_1 = 1
    xn, _ = Quasi_Newton(funct, val_1)
    assert np.isclose(xn, 5, tolerance)
    
    
def test_quasinewton_vector():
    def funct_vect(values):
        var1 = Variable(name='x',value=values[0])
        var2 = Variable(name='y',value=values[1])
        f = (1.-var1)**2. + (var2-var1*var1)**2.

        return f
    
    val_1 = 0.1
    val_2 = 0.2
    xn, _ = Quasi_Newton(funct_vect, x0=np.array([val_1, val_2]))
    
    
    assert np.isclose(np.mean(xn), 1, tolerance)
