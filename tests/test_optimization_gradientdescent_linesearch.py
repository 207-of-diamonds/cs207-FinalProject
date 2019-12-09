import sys
sys.path.append('..')
import pytest
import bitterdispute.elementary_functions as elem
import bitterdispute.variable as Variable
import bitterdispute.optimization_gradientdescent_linesearch as opt
import numpy as np

## gradient descent
def test_GD_singleVariable():
    def f(val):
        x1 = Variable('x',val)
        # x2 = Variable('y',val[1])
        f = (x1-5) ** 2
        return f
    a = opt.gradientDescent(f,init_val=[3])
    assert a[0] < 100
    assert np.isclose(a[1][0], 5, atol=1e-4)

def test_GD_multiVariable():
    def f(val):
        x1 = Variable('x',val[0])
        x2 = Variable('y',val[1])
        f = (x1-5) ** 2 + (x2-5) ** 2
        return f
    a = opt.gradientDescent(f,init_val=[3,1])
    assert a[0] < 100
    assert np.isclose(a[1][0], 5, atol=1e-4)
    assert np.isclose(a[1][1], 5, atol=1e-4)


# def f(val):
#     x1 = Variable('x',val[0])
#     x2 = Variable('y',val[1])
#     f = (x1-5) ** 2 + x2
#     return f
# a = gradientDescent(f,init_val=[3,1])

# def f(val):
#     x1 = sc.Scalar(val)
#     #x2 = Scalar(values)
#     f = (x1-5) ** 2 #+ x2
#     return f
# a = opt.gradientDescent(f,init_val=3)

def test_bLS():
    def f(val):
        x1 = sc.Scalar(val)
        #x2 = Scalar(values)
        f = (x1-5) ** 2 #+ x2
        return f
    a = opt.backtrackingLineSearch(f, init_val=6)
    b = opt.backtrackingLineSearch(f, init_val=5)
    c = opt.backtrackingLineSearch(f, init_val=1)
    assert c[1] < a[1] < b[1]

# def f(val):
#     x1 = sc.Scalar(val)
#     f = (x1-5) ** 2
#     return f
# a = opt.backtrackingLineSearch(f, init_val=6)
# b = opt.backtrackingLineSearch(f, init_val=5)
# c = opt.backtrackingLineSearch(f, init_val=1)
