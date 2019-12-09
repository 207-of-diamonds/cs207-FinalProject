import pytest
import numpy as np
from bitterdispute.variable import Variable

def test_start_results():
    x = Variable('x', 5)
    assert x.name == 'x'
    assert x.val == 5
    assert x.der['x'] == 1
    assert x.der2['x'] == 0

def test_str():
    x = Variable('x', 5)
    assert x.__str__() == '5'

def test_add_results():
    x1 = Variable('x', 1)
    x2 = x1 + 4
    x3 = 4 + x1 # test __radd__
    x3 = -x1 + 5 # test __neg__
    x4 = Variable('y', 4)
    x5 = x1 + x4
    assert x2.val == 5
    assert x2.der['x'] == 1
    assert x2.der2['x'] == 0
    assert x3.val == 4
    assert x3.der['x'] == -1
    assert x3.der2['x'] == 0
    assert x5.val == 5
    assert x5.der['x'] == 1
    assert x5.der['y'] == 1
    assert x5.der2['x'] == 0
    assert x5.der2['y'] == 0

def test_sub_results():
    x1 = Variable('x', 4)
    x2 = x1 - 3
    x3 = x2 - x1
    x4 = 5 - x1 # test __rsub__
    x5 = Variable('y', 4)
    x6 = x1 + x5
    assert x2.val == 1
    assert x2.der['x'] == 1
    assert x2.der2['x'] == 0
    assert x3.val == -3
    assert x3.der['x'] == 0
    assert x3.der2['x'] == 0
    assert x4.val == 1
    assert x4.der['x'] == -1
    assert x4.der2['x'] == 0
    assert x6.val == 8
    assert x6.der['x'] == 1
    assert x6.der['y'] == 1
    assert x6.der2['x'] == 0
    assert x6.der2['y'] == 0

def test_mul_results():
    x1 = Variable('x', 5)
    x2 = 3*x1
    x3 = x1*x2
    x4 = x3*5 # test __rmul__
    x5 = Variable('y', 4)
    x6 = x1*x5
    assert x2.val == 15
    assert x2.der['x'] == 3
    assert x2.der2['x'] == 0
    assert x3.val == 75
    assert x3.der['x'] == 30
    assert x3.der2['x'] == 6
    assert x4.val == 375
    assert x4.der['x'] == 150
    assert x4.der2['x'] == 30
    assert x6.val == 20
    assert x6.der['x'] == 4
    assert x6.der['y'] == 5
    assert x6.der2['x'] == 0
    assert x6.der2['y'] == 0
    
def test_div_results():
    x1 = Variable('x', 1)
    x2 = x1/4
    x3 = x1/x2
    x4 = 2/x1 # test __rtruediv__
    x5 = Variable('y', 1)
    x6 = x1/x5
    assert x2.val == 1/4
    assert x2.der['x'] == 1/4
    assert x2.der2['x'] == 0
    assert x3.val == 4
    assert x3.der['x'] == 0
    assert x3.der2['x'] == 0
    assert x4.val == 2
    assert x4.der['x'] == -2
    assert x4.der2['x'] == 4
    assert x6.val == 1
    assert x6.der['x'] == 1
    assert x6.der['y'] == -1
    assert x6.der2['x'] == 0
    assert x6.der2['y'] == 2
    
def test_pow_results():
    x1 = Variable('x', 2)
    x2 = x1**2
    x3 = 4**x1 # test __rpow__
    assert x2.val == 4
    assert x2.der['x'] == 4
    assert x2.der2['x'] == 2
    assert x3.val == 16
    assert np.isclose(x3.der['x'], np.log(4)*4**2)
    assert np.isclose(x3.der2['x'], 4**2*(np.log(4)**2))
    
def test_add_types():
    with pytest.raises(TypeError):
        Variable('x', "hi") + 5
    assert Variable('x', 5) + "hi" is None

def test_sub_types():
    with pytest.raises(TypeError):
        Variable('x', "hi") - 5
    assert Variable('x', 5) - "hi" is None
        
def test_mul_types():
    with pytest.raises(TypeError):
        Variable('x', "hi") * 5
    assert Variable('x', 5) * "hi" is None
        
def test_div_types():
    with pytest.raises(TypeError):
        Variable('x', "hi") / 5
    assert Variable('x', 5) / "hi" is None
        
def test_pow_types():
    with pytest.raises(TypeError):
        Variable('x', "hi") / 5
    assert Variable('x', 5) ** "hi" is None
        
def test_eq_results():
    x1 = Variable('x', 1)
    x2 = Variable('y', 1)
    x3 = 1
    assert(x1 == x2)
    assert(x1 == x3)
    assert(not (x1 != x2))
    assert(not (x1 != x3))

    
def test_lt_results():
    x1 = Variable('x', 1)
    x2 = Variable('y', 2)
    x3 = 2
    assert(x1 < x2)
    assert(x1 < x3)
    assert(not (x1 > x2))
    assert(not (x1 > x3))
    
def test_le_results():
    x1 = Variable('x', 2)
    x2 = Variable('y', 2)
    x3 = 2
    assert(x1 <= x2)
    assert(x1 <= x3)
    assert(not (x1 < x2))
    assert(not (x1 < x3))
    
def test_gt_results():
    x1 = Variable('x', 4)
    x2 = Variable('y', 2)
    x3 = 2
    assert(x1 > x2)
    assert(x1 > x3)
    assert(not (x1 < x2))
    assert(not (x1 < x3))
    
def test_ge_results():
    x1 = Variable('x', 4)
    x2 = Variable('y', 4)
    x3 = 4
    assert(x1 >= x2)
    assert(x1 >= x3)
    assert(not (x1 > x2))
    assert(not (x1 > x3))