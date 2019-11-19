'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute,
focusing on functions in scalar.py.
'''
import pytest
import numpy as np
import bitterdispute.scalar as sc

def test_start():
    x = sc.Scalar(5)
    assert x.val == 5
    assert x.der == 1

def test_add():
    x1 = sc.Scalar(1)
    x2 = x1 + 4
    x3 = 4 + x1
    x3 = -x1 + 5 # TEST_NEG__
    x4 = sc.Scalar(4)
    x5 = x1 + x4
    assert x2.val == 5
    assert x2.der == 1
    assert x3.val == 4
    assert x3.der == -1
    assert x5.val == 5
    assert x5.der == 2

def test_sub():
    x1 = sc.Scalar(4)
    x2 = x1 - 3
    x3 = x2 - x1
    x4 = 5 - x1
    x5 = x1 - 3
    assert x2.val == 1
    assert x2.der == 1
    assert x3.val == -3
    assert x3.der == 0
    assert x4.val == 1
    assert x4.der == -1
    assert x5.val == 1
    assert x5.der == 1

def test_mul():
    x1 = sc.Scalar(5)
    x2 = 3*x1
    x3 = x1*x2
    x4 = x3*5
    assert x2.val == 15
    assert x2.der == 3
    assert x3.val == 75
    assert x3.der == 30
    assert x4.val == 375
    assert x4.der == 150

def test_div():
    x1 = sc.Scalar(1)
    x2 = x1/4
    x3 = x1/x2
    x4 = 2/x1
    assert x2.val == 1/4
    assert x2.der == 1/4
    assert x3.val == 4
    assert x3.der == 0
    assert x4.val == 2
    assert x4.der == -2

def test_pow():
    x1 = sc.Scalar(2)
    x2 = x1**2
    x3 = 4**x1 # test __rpow__
    x4 = x2 ** x1
    assert x2.val == 4
    assert x2.der == 4
    assert x3.val == 16
    assert x3.der == np.log(4)*4**2
    assert x4.val == 16
    assert round(x4.der, 10) == round(120.722839111673, 10)

# test_add()
# test_sub()
# test_mul()
# test_div()
# test_pow()
