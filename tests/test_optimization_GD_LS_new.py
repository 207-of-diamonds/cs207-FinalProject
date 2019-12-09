import sys
sys.path.append('..')
import pytest
import bitterdispute.elementary_functions as elem
import bitterdispute.variable as Variable
import bitterdispute.optimization_GD_LS_new as opt
import numpy as np

## gradient descent
# if input is not a list
def test_GD_type():
    with pytest.raises(TypeError):
        def f(val):
            x1 = Variable('x',val)
            f = (x1-5) ** 2
            return f
        a = opt.gradientDescent(f,init_val='hello')

#single variable
def test_GD_singleVariable():
    def f(val):
        x1 = Variable('x',val)
        f = (x1-5) ** 2
        return f
    a = opt.gradientDescent(f,init_val=[3])
    assert np.isclose(a[1], 5, atol=1e-4)

#multi variable
def test_GD_multiVariable():
    def f(val):
        x1 = Variable('x',val[0])
        x2 = Variable('y',val[1])
        f = (x1-5) ** 2 + (x2-5) ** 2
        return f
    a = opt.gradientDescent(f,init_val=[3,1])

    assert np.isclose(a[1], 5, atol=1e-4)
    assert np.isclose(a[1], 5, atol=1e-4)

## backtracking line search
# single variable
def test_bLS_singleVariable():
    def f(val):
        x1 = Variable('x',val[0])
        #x2 = Scalar(values)
        f = (x1-5) ** 2
        return f
    a = opt.backtrackingLineSearch(f, init_val=[6])
    b = opt.backtrackingLineSearch(f, init_val=[5])
    assert a[1][0] < b[1][0]
# multivariable
def test_bLS_multiVariable():
    def f(val):
        x1 = Variable('x',val[0])
        x2 = Variable('y',val[1])
        f = (x1-5) ** 2
        return f
    a = opt.backtrackingLineSearch(f, init_val=[6,6])
    b = opt.backtrackingLineSearch(f, init_val=[5,5])
    assert a[1][0] < b[1][0]

# def f(val):
#     x1 = Variable('x',val[0])
#     x2 = Variable('y',val[1])
#     f = (x1-5) ** 2 + (x2-5)**2
#     return f
# a = backtrackingLineSearch(f, init_val=[7,7])
# b = backtrackingLineSearch(f, init_val=[5,5])

# def f(val):
#     x1 = Variable('x',val[0])
#     f = (x1-5) ** 2
#     return f
# a = backtrackingLineSearch(f, init_val=[7])
# b = backtrackingLineSearch(f, init_val=[5])
