import pytest
import bitterdispute.elementary_functions as elem
from bitterdispute.variable import Variable
import numpy as np

## sin ======================
def test_sin_result_constant():
    assert np.isclose(elem.sin(1.0), np.sin(1.0))

def test_sin_result_var():
    val = 1
    x = Variable('x', val)
    obj_generate = elem.sin(x)
    obj_wanted = Variable(name='x', value=np.sin(val), 
                          derivative=np.cos(val), second_derivative=-np.sin(val))
    
    assert np.isclose(obj_generate.val, obj_wanted.val)

    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0


def test_cos_types():
    with pytest.raises(TypeError):
        elem.cos("hi")

## tan ======================
def test_tan_result_constant():
    assert elem.tan(1.0) == np.tan(1.0)

def test_tan_result_var():
    val = 1
    x = Variable('x', val)
    obj_generate = elem.tan(x)
    obj_wanted = Variable(name='x', value=np.tan(val), derivative=1/(np.cos(val))**2, second_derivative=2*np.tan(x)*(1/np.cos(x))**2)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert list(obj_generate.der) == list(obj_wanted.der)
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_tan_types():
    with pytest.raises(TypeError):
        elem.tan("hi")

## log ======================
def test_log_result_constant():
    assert np.isclose(elem.log(1.0), np.log(1.0))

def test_log_result_var():
    val = 1
    x = Variable('x', val)
    obj_generate = elem.log(x)
    obj_wanted = Variable(name='x', value=np.log(val), derivative=1/(val), second_derivative=-1/(val)**2)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert list(obj_generate.der) == list(obj_wanted.der)
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_log_input_var_notvalid():
    val = -2
    x = Variable('x', val)
    with pytest.raises(ValueError):
        obj_generate = elem.log(x)
    
def test_log_types():
    with pytest.raises(TypeError):
        elem.log("hi")
        
        
## sqrt ======================
def test_sqrt_result_constant():
    assert np.isclose(elem.sqrt(10.0), np.sqrt(10.0))

def test_sqrt_result_var():
    val = 4
    x = Variable('x', val)
    obj_generate = elem.sqrt(x)
    obj_wanted = Variable(name='x', value=np.sqrt(val), derivative=1/(2*np.sqrt(x.val)), second_derivative=-1/(4*val**(3/2)))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    assert list(obj_generate.der) == list(obj_wanted.der)
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

    
def test_sqrt_input_var_notvalid():
    val = -2
    x = Variable('x', val)
    with pytest.raises(ValueError):
        obj_generate = elem.sqrt(x)
        
def test_sqrt_types():
    with pytest.raises(TypeError):
        elem.sqrt("hi")

def test_sin_types():
    with pytest.raises(TypeError):
        elem.sin("hi")
        
        
## arcsin ======================
def test_arcsin_result_constant():
    assert np.isclose(elem.arcsin(1.0), np.arcsin(1.0))

####### need check valid range
def test_arcsin_result_constant_notvalid():
    with pytest.raises(ValueError):
        elem.arcsin(2.0)

def test_arcsin_result_var():
    val = 0
    x = Variable('x', val)
    obj_generate = elem.arcsin(x)
    obj_wanted = Variable('x', np.arcsin(val), 1/np.sqrt(1-val**2), val/(1-val**2)**(3/2))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0


####### need check valid range
def test_arcsin_result_var_notvalid():
    val = 2
    x = Variable('x',val)
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
    x = Variable('x',val)
    obj_generate = elem.arccos(x)
    obj_wanted = Variable('x',np.arccos(val), -1/np.sqrt(1-val**2), -val/(1-val**2)**(3/2))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0


####### need check valid range
def test_arccos_result_var_notvalid():
    val = 2
    x = Variable('x',val)
    with pytest.raises(ValueError):
        obj_generate = elem.arccos(x)

def test_arccos_types():
    with pytest.raises(TypeError):
        elem.arccos("hi")

# arctan ======================
def test_arctan_result_constant():
    assert np.isclose(elem.arctan(1.0), np.arctan(1.0))

def test_arctan_result_var():
    val = 1
    x = Variable('x', val)
    obj_generate = elem.arctan(x)
    obj_wanted = Variable('x', np.arctan(val), 1/(val**2+1), -2*val/(val**2+1)**2)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_arctan_types():
    with pytest.raises(TypeError):
        elem.arctan("hi")
        
        
## exp ======================
def test_exp_result_constant():
    assert np.isclose(elem.exp(1.0), np.exp(1.0))

def test_exp_result_var():
    val = 1
    x = Variable('x', val)
    obj_generate = elem.exp(x)
    obj_wanted = Variable('x', np.exp(val), np.exp(val),np.exp(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_exp_types():
    with pytest.raises(TypeError):
        elem.exp("hi")

        

## sinh ======================
def test_sinh_result_constant():
    assert np.isclose(elem.sinh(1.0), np.sinh(1.0))

def test_sihn_result_var():
    val = 1
    x = Variable('x',val)
    obj_generate = elem.sinh(x)
    obj_wanted = Variable(name='x', value = np.sinh(val), 
                          derivative = np.cosh(val), second_derivative=np.sinh(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_sinh_types():
    with pytest.raises(TypeError):
        elem.sinh("hi")
        
## cosh ======================
def test_cosh_result_constant():
    assert np.isclose(elem.cosh(1.0), np.cosh(1.0))

def test_cosh_result_var():
    val = 1
    x = Variable('x',val)
    obj_generate = elem.cosh(x)
    obj_wanted = Variable(name='x', value= np.cosh(val), 
                          derivative = np.sinh(val), second_derivative=np.cosh(val))
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0

def test_cosh_types():
    with pytest.raises(TypeError):
        elem.cosh("hi")

## tanh ======================
def test_tanh_result_constant():
    assert np.isclose(elem.tanh(1.0), np.tanh(1.0))

def test_tanh_result_var():
    val = 1
    x = Variable('x',val)
    obj_generate = elem.tanh(x)
    obj_wanted = Variable(name='x', value=np.tanh(val), 
                          derivative = (1/np.cosh(val))**2, second_derivative=-2*np.sinh(val)/(np.cosh(val))**3)
    assert np.isclose(obj_generate.val, obj_wanted.val)
    ## ensure same element
    assert list(obj_generate.der)==list(obj_wanted.der)  
    ## ensure same value
    assert sum(list(map(lambda x: not np.isclose(obj_generate.der[x], obj_wanted.der[x]), obj_generate.der)))==0
    
def test_tanh_types():
    with pytest.raises(TypeError):
        elem.tanh("hi")
