import sys
sys.path.append('..')
import pytest
import bitterdispute.elementary_functions as elem
from bitterdispute.variable import Variable
import bitterdispute.optimization_gradientdescent_linesearch as opt
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
    assert np.isclose(a[1], 5, atol=1e-2)

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
    assert a[1] > b[1]
