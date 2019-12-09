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
    assert x.values == [41]
    assert x.derivatives == [{'x': 4.0, 'y': 7.0}]
    assert x.formulas == ['4*x+7*y']

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
    assert x.values == [-33]
    assert x.derivatives == [{'z': 0.5, 'x': -0.0625, 'y': -7.0}]
    assert x.formulas == ['4/x-7*y+z/2']

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
    assert [round(val, 10) for val in x.values] == [round(10.925144543414053, 10)]
    assert x.derivatives == [{'y': 0.0007263329237752267, 'x': -1.0185002366602949}]
    assert x.formulas == ['sin(x)*7+4*tanh(y)']

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
    assert [round(val, 10) for val in x.values] == [round(-0.18607529153476626, 10)]
    assert x.derivatives == [{'y': 3.046986001124803, 'z': -0.09194869423196683, 'x': 46.91292723071239}]
    assert x.formulas == ['sin(cos(tan(x)*y)*z)']

def test_power(mocker):
    """
    Test for handling power operations with 1 variable
    Formula: 'x**5'
    Values:
        x = 3
    """
    mocker.patch('builtins.input', side_effect=[1, 3, 'x**5'])
    x = AD()
    assert x.values == [243]
    assert x.derivatives == [{'x': 405.0}]
    assert x.formulas == ['x**5']

def test_positive(mocker):
    """
    Test for handling positive and negative conversions
    Formula: '-x+3*(y)'
    Values:
        x = 8
        y = 2
    """
    mocker.patch('builtins.input', side_effect=[2, 2, 8, '-x+3*(y)'])
    x = AD()
    assert x.values == [-2]
    assert x.derivatives == [{'x': -1, 'y': 3.0}]
    assert x.formulas == ['-x+3*(y)']

# def test_print(mocker): todo if time
#     """
#     """
#     mocker.patch('builtins.input', side_effect=[2, 3, 5, '-x+3*(y)'])
#     x = AD()
#     print(x)
#     assert mock_stdout.getvalue() == """
#         Welcome to Bitter Dispute! America's favorite automatically
#             differentiating gameshow. Let's get started.
#
#         Great, we'll use 2 variables.
#         Please enter a value for variable number 1.
#         Please enter a value for variable number 2.
#         Thank you, we recorded these values:
#         y = 3.0
#         x = 5.0
#         Lastly, what formulas would you like to derive? Please use the variables just listed.        You may enter as many formulas as you'd like as a list!
#         The final derivative of formula ['-x+3*(y)'] with your chosen values is [{'x': -1, 'y': 3.0}]. Thanks for playing!
#
#             Formula(s) saved: ['-x+3*(y)'],
#             Value(s) used: [4.0],
#             Derivatives found: [{'x': -1, 'y': 3.0}]
#     """
