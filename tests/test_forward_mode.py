'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute.
'''
# Import necessary modules
import pytest
from bitterdispute.forward_mode import AD

def test_standard_formula1(mocker, capsys):
    """
    Test for handling standard scalar operations with two variables
    Test for print statement functioning
    Formula: '4*x+7*y'
    Values:
        x = 3
        y = 5
    """
    mocker.patch('builtins.input', side_effect=[2, 3, 5, '4*x+7*y'])
    x = AD()
    assert x.val == 41
    assert x.der == 11
    assert x.formula == '4*x+7*y'

def test_standard_formula2(mocker):
    """
    Test for handling standard scalar operations with three variables
    Formula: '4/x-7*y+z/2'
    Values:
        x = 8
        y = 5
        z = 3
    """
    mocker.patch('builtins.input', side_effect=[3, 3, 5, 8, '4/x-7*y+z/2'])
    x = AD()
    assert x.val == -33
    assert x.der == -6.5625
    assert x.formula == '4/x-7*y+z/2'

def test_elementary_functions1(mocker):
    """
    Test for handling elementary operations with two variables
    Formula: 'sin(x)*7+4*tanh(y)'
    Values:
        x = 8
        y = 5
    """
    mocker.patch('builtins.input', side_effect=[2, 5, 8, 'sin(x)*7+4*tanh(y)'])
    x = AD()
    assert x.val == 10.925144543414053
    assert x.der == -1.0177739037365197
    assert x.formula == 'sin(x)*7+4*tanh(y)'

def test_elementary_functions2(mocker):
    """
    Test for handling elementary operations with three variables
    Formula: 'sin(cos(tan(x)*y)*z)'
    Values:
        x = 1
        y = 7
        z = 2
    """
    mocker.patch('builtins.input', side_effect=[3, 2, 7, 1, 'sin(cos(tan(x)*y)*z)'])
    x = AD()
    assert x.val == -0.18607529153476626
    assert x.der == 49.86796453760523
    assert x.formula == 'sin(cos(tan(x)*y)*z)'

def test_power(mocker):
    """
    Test for handling power operations with 1 variable
    Formula: 'x**5'
    Values:
        x = 3
    """
    mocker.patch('builtins.input', side_effect=[1, 3, 'x**5'])
    x = AD()
    assert x.val == 243.0
    assert x.der == 405.0
    assert x.formula == 'x**5'

def test_positive(mocker):
    """
    Test for handling positive and negative conversions
    Formula: '+(-x+3*(y))'
    Values:
        x = 8
        y = 2
    """
    mocker.patch('builtins.input', side_effect=[2, 2, 8, '+(-x+3*(y))'])
    x = AD()
    assert x.val == -2.0
    assert x.der == 2.0
    assert x.formula == '+(-x+3*(y))'


def test_really_big_numbers(mocker):
    """
    Test for handling overly large input values or derived values during operations
    Formula: sin(x*y*z)**tanh(z)
    Values:
        z = 4.6
        y = 9.2
        x = 5.0
    Error: RuntimeWarning: invalid value encountered in log
    Returns nan - TODO Should we handle this or change error message?
    Reference: https://stackoverflow.com/questions/27784528/numpy-division-with-runtimewarning-invalid-value-encountered-in-double-scalars
    """
    pass
