'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute,
focusing on functions in elementary_functions.py.
'''
# pytest .\test_roots.py
import pytest
import bitterdispute.elementary_functions as elem
import bitterdispute.scalar as sc
import numpy as np

## sin ======================
def test_sin_result_constant():
    assert np.isclose(elem.sin(1.0), np.sin(1.0))

def test_sin_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.sin(x)
    obj_wanted = sc.Scalar(np.sin(val), np.cos(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_sin_types():
    with pytest.raises(TypeError):
        elem.sin("hi")

## cos ======================
def test_cos_result_constant():
    assert np.isclose(elem.cos(1.0), np.cos(1.0))

def test_cos_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.cos(x)
    obj_wanted = sc.Scalar(np.cos(val), -np.sin(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_cos_types():
    with pytest.raises(TypeError):
        elem.cos("hi")


## tan ======================
def test_tan_result_constant():
    assert elem.tan(1.0) == np.tan(1.0)

def test_tan_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.tan(x)
    obj_wanted = sc.Scalar(np.tan(val), 1/(np.cos(val))**2)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_tan_types():
    with pytest.raises(TypeError):
        elem.tan("hi")

## arcsin ======================
def test_arcsin_result_constant():
    assert np.isclose(elem.arcsin(1.0), np.arcsin(1.0))

####### need check valid range
def test_arcsin_result_constant_notvalid():
    with pytest.raises(ValueError):
        elem.arcsin(2.0)

def test_arcsin_result_var():
    val = 0
    x = sc.Scalar(val)
    obj_generate = elem.arcsin(x)
    obj_wanted = sc.Scalar(np.arcsin(val), 1/np.sqrt(1-val**2))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

####### need check valid range
def test_arcsin_result_var_notvalid():
    val = 2
    x = sc.Scalar(val)
    with pytest.raises(ValueError):
        obj_generate = elem.arcsin(x)

def test_arcsin_types():
    with pytest.raises(TypeError):
        elem.arcsin("hi")

## arccos ======================
def test_arccos_result_constant():
    assert np.isclose(elem.arccos(1.0), np.arccos(1.0))

####### need check valid range
def test_arccos_result_constant_notvalid():
    with pytest.raises(ValueError):
        elem.arccos(2.0)

def test_arccos_result_var():
    val = 0
    x = sc.Scalar(val)
    obj_generate = elem.arccos(x)
    obj_wanted = sc.Scalar(np.arccos(val), -1/np.sqrt(1-val**2))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

####### need check valid range
def test_arccos_result_var_notvalid():
    val = 2
    x = sc.Scalar(val)
    with pytest.raises(ValueError):
        obj_generate = elem.arccos(x)

def test_arccos_types():
    with pytest.raises(TypeError):
        elem.arccos("hi")

## arctan ======================
def test_arctan_result_constant():
    assert np.isclose(elem.arctan(1.0), np.arctan(1.0))

def test_arctan_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.arctan(x)
    obj_wanted = sc.Scalar(np.arctan(val), 1/(val**2+1))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_arctan_types():
    with pytest.raises(TypeError):
        elem.arctan("hi")

## sinh ======================
def test_sinh_result_constant():
    assert np.isclose(elem.sinh(1.0), np.sinh(1.0))

def test_sihn_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.sinh(x)
    obj_wanted = sc.Scalar(np.sinh(val), np.cosh(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_sinh_types():
    with pytest.raises(TypeError):
        elem.sinh("hi")

## cosh ======================
def test_cosh_result_constant():
    assert np.isclose(elem.cosh(1.0), np.cosh(1.0))

def test_cosh_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.cosh(x)
    obj_wanted = sc.Scalar(np.cosh(val), np.sinh(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_cosh_types():
    with pytest.raises(TypeError):
        elem.cosh("hi")

## tanh ======================
def test_tanh_result_constant():
    assert np.isclose(elem.tanh(1.0), np.tanh(1.0))

def test_tanh_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.tanh(x)
    obj_wanted = sc.Scalar(np.tanh(val), (1/np.cosh(val))**2)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_tanh_types():
    with pytest.raises(TypeError):
        elem.tanh("hi")

## exp ======================
def test_exp_result_constant():
    assert np.isclose(elem.exp(1.0), np.exp(1.0))

def test_exp_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.exp(x)
    obj_wanted = sc.Scalar(np.exp(val), np.exp(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_exp_types():
    with pytest.raises(TypeError):
        elem.exp("hi")

## log ======================
def test_log_result_constant():
    assert np.isclose(elem.log(1.0), np.log(1.0))

def test_log_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.log(x)
    obj_wanted = sc.Scalar(np.log(val), 1/(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_log_types():
    with pytest.raises(TypeError):
        elem.log("hi")

## sqrt ======================
def test_sqrt_result_constant():
    assert np.isclose(elem.sqrt(10.0), np.sqrt(10.0))

def test_sqrt_result_var():
    val = 4
    x = sc.Scalar(val)
    obj_generate = elem.sqrt(x)
    obj_wanted = sc.Scalar(np.sqrt(val), 1/(2*np.sqrt(x.val)))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert np.isclose(obj_generate.der, obj_wanted.der)

def test_sqrt_types():
    with pytest.raises(TypeError):
        elem.sqrt("hi")