'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute,
focusing on functions in scalar.py.
'''
import pytest
import numpy as np
import bitterdispute.scalar as sc

def test_start_results():
    x = sc.Scalar(5)
    assert x.val == 5
    assert x.der == 1
    assert x.der2 == 0

def test_str():
    x = sc.Scalar(5)
    assert x.__str__() == '5'
    
def test_add_results():
    x1 = sc.Scalar(1)
    x2 = x1 + 4
    x3 = 4 + x1 # test __radd__
    x3 = -x1 + 5 # test __neg__
    x4 = sc.Scalar(4)
    x5 = x1 + x4
    assert x2.val == 5
    assert x2.der == 1
    assert x2.der2 == 0
    assert x3.val == 4
    assert x3.der == -1
    assert x3.der2 == 0
    assert x5.val == 5
    assert x5.der == 2
    assert x5.der2 == 0

def test_sub_results():
    x1 = sc.Scalar(4)
    x2 = x1 - 3
    x3 = x2 - x1
    x4 = 5 - x1 # test __rsub__
    x5 = x1 - 3
    assert x2.val == 1
    assert x2.der == 1
    assert x2.der2 == 0
    assert x3.val == -3
    assert x3.der == 0
    assert x3.der2 == 0
    assert x4.val == 1
    assert x4.der == -1
    assert x4.der2 == 0
    assert x5.val == 1
    assert x5.der == 1
    assert x5.der2 == 0

def test_mul_results():
    x1 = sc.Scalar(5)
    x2 = 3*x1
    x3 = x1*x2
    x4 = x3*5 # test __rmul__
    assert x2.val == 15
    assert x2.der == 3
    assert x2.der2 == 0
    assert x3.val == 75
    assert x3.der == 30
    assert x3.der2 == 6
    assert x4.val == 375
    assert x4.der == 150
    assert x4.der2 == 30

def test_div_results():
    x1 = sc.Scalar(1)
    x2 = x1/4
    x3 = x1/x2
    x4 = 2/x1 # test __rtruediv__
    assert x2.val == 1/4
    assert x2.der == 1/4
    assert x2.der2 == 0
    assert x3.val == 4
    assert x3.der == 0
    assert x3.der2 == 0
    assert x4.val == 2
    assert x4.der == -2
    assert x4.der2 == 4

def test_pow_results():
    x1 = sc.Scalar(2)
    x2 = x1**2
    x3 = 4**x1 # test __rpow__
    x4 = sc.Scalar(4) ** sc.Scalar(2) 
    assert x2.val == 4
    assert x2.der == 4
    assert x2.der2 == 2
    assert x3.val == 16
    assert np.isclose(x3.der, np.log(4)*4**2)
    assert np.isclose(x3.der2, 4**2*(np.log(4)**2))
    assert x4.val == 16
    assert np.isclose(x4.der, 2*(4**1) + np.log(4)*4**2)
    assert np.isclose(x4.der2, (4**2)*((2/4) + np.log(4)*1)**2 + (4 ** 2)*((2*1*1/4) - (2*(1**2)/(4**2))))
    
def test_add_types():
    with pytest.raises(TypeError):
        sc.Scalar("hi") + 5
    assert str(sc.Scalar(5) + "hi") == 'None'

def test_sub_types():
    with pytest.raises(TypeError):
        sc.Scalar("hi") - 5
    assert str(sc.Scalar(5) - "hi") == 'None'
        
def test_mul_types():
    with pytest.raises(TypeError):
        sc.Scalar("hi") * 5
    assert str(sc.Scalar(5) * "hi") == 'None'
        
def test_div_types():
    with pytest.raises(TypeError):
        sc.Scalar("hi") / 5
    assert str(sc.Scalar(5) / "hi") == 'None'
        
def test_pow_types():
    with pytest.raises(TypeError):
        sc.Scalar("hi") ** 5
    assert str(sc.Scalar(5) ** "hi") == 'None'
        
def test_eq_results():
    x1 = sc.Scalar(1)
    x2 = sc.Scalar(1)
    x3 = 1
    assert(x1 == x2)
    assert(x1 == x3)
    assert(not (x1 != x2))
    assert(not (x1 != x3))

    
def test_lt_results():
    x1 = sc.Scalar(1)
    x2 = sc.Scalar(2)
    x3 = 2
    assert(x1 < x2)
    assert(x1 < x3)
    assert(not (x1 > x2))
    assert(not (x1 > x3))
    
def test_le_results():
    x1 = sc.Scalar(2)
    x2 = sc.Scalar(2)
    x3 = 2
    assert(x1 <= x2)
    assert(x1 <= x3)
    assert(not (x1 < x2))
    assert(not (x1 < x3))
    
def test_gt_results():
    x1 = sc.Scalar(4)
    x2 = sc.Scalar(2)
    x3 = 2
    assert(x1 > x2)
    assert(x1 > x3)
    assert(not (x1 < x2))
    assert(not (x1 < x3))
    
def test_ge_results():
    x1 = sc.Scalar(4)
    x2 = sc.Scalar(4)
    x3 = 4
    assert(x1 >= x2)
    assert(x1 >= x3)
    assert(not (x1 > x2))
    assert(not (x1 > x3))