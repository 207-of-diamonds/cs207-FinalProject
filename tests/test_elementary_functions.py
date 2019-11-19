# pytest .\test_roots.py
import pytest
import elementary_functions as elem
import scalar as sc
import numpy as np

## sin ======================
def test_sin_result_constant():
    assert elem.sin(1.0) == np.sin(1.0)

def test_sin_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.sin(x) 
    obj_wanted = sc.Scalar(np.sin(val), np.cos(val))
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

def test_sin_types():
    with pytest.raises(TypeError):
        elem.sin("hi")
        
## cos ======================
def test_cos_result_constant():
    assert elem.cos(1.0) == np.cos(1.0)

def test_cos_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.cos(x) 
    obj_wanted = sc.Scalar(np.cos(val), -np.sin(val))
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

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
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

def test_tan_types():
    with pytest.raises(TypeError):
        elem.tan("hi")
        
## arcsin ======================
def test_arcsin_result_constant():
    assert elem.arcsin(1.0) == np.arcsin(1.0)

####### need check valid range
def test_arcsin_result_constant_notvalid():
    with pytest.raises(ValueError):
        elem.arcsin(2.0) 

def test_arcsin_result_var():
    val = 0
    x = sc.Scalar(val)
    obj_generate = elem.arcsin(x) 
    obj_wanted = sc.Scalar(np.arcsin(val), 1/np.sqrt(1-val**2))
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

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
    assert elem.arccos(1.0) == np.arccos(1.0)

####### need check valid range
def test_arccos_result_constant_notvalid():
    with pytest.raises(ValueError):
        elem.arccos(2.0) 

def test_arccos_result_var():
    val = 0
    x = sc.Scalar(val)
    obj_generate = elem.arccos(x) 
    obj_wanted = sc.Scalar(np.arccos(val), -1/np.sqrt(1-val**2))
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

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
    assert elem.arctan(1.0) == np.arctan(1.0)

def test_arctan_result_var():
    val = 1
    x = sc.Scalar(val)
    obj_generate = elem.arctan(x) 
    obj_wanted = sc.Scalar(np.arctan(val), 1/(val**2+1))
    assert obj_generate.val == obj_wanted.val
    assert obj_generate.der == obj_wanted.der

def test_arctan_types():
    with pytest.raises(TypeError):
        elem.arctan("hi")
 