'''
This file contains a number of unit tests
to confirm proper errors and behavior during our Bitter Dispute.
'''
# Import necessary modules
import pytest
from bitterdispute.forward_mode import AD

def test_standard_formula1(mocker):
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
    assert x.outputs == [41]
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
    assert x.outputs == [-33]
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
    for li in x.derivatives:
        for key, value in li.items():
            li[key] = round(value, 5)
    assert [round(val, 5) for val in x.outputs] == [round(10.925144543414053, 5)]
    assert x.derivatives == [{'y': 0.00073, 'x': -1.0185}]
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
    for li in x.derivatives:
        for key, value in li.items():
            li[key] = round(value, 5)
    assert [round(val, 5) for val in x.outputs] == [round(-0.18607529153476626, 5)]
    assert x.derivatives == [{'x': 46.91293, 'y': 3.04699, 'z': -0.09195}]
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
    assert x.outputs == [243]
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
    assert x.outputs == [-2]
    assert x.derivatives == [{'x': -1, 'y': 3.0}]
    assert x.formulas == ['-x+3*(y)']

def test_new_values(mocker):
    """todo
    """
    mocker.patch('builtins.input', side_effect=[2, 2, 8, 'sin(x)*7+4*tanh(y)'])
    x = AD()
    mocker.patch('builtins.input', side_effect=[5, 8])
    x.new_values()
    for li in x.derivatives:
        for key, value in li.items():
            li[key] = round(value, 5)
    assert x.inputs == {'y': 5.0, 'x': 8.0}
    assert [round(val, 5) for val in x.outputs] == [round(10.925144543414053, 5)]
    assert x.derivatives == [{'x': -1.0185, 'y': 0.00073}]
    assert x.formulas == ['sin(x)*7+4*tanh(y)']

def test_new_formulas(mocker):
    """todo
    """
    mocker.patch('builtins.input', side_effect=[2, 2, 8, 'sin(x)*7+4*tanh(y)'])
    x = AD()
    mocker.patch('builtins.input', side_effect=['cos(x)*y+13-x**2'])
    x.new_formulas()
    for li in x.derivatives:
        for key, value in li.items():
            li[key] = round(value, 5)
    assert x.inputs == {'y': 2.0, 'x': 8.0}
    assert [ round(elem, 5) for elem in x.outputs ] == [ round(elem, 5) for elem in [-51.291000067617226] ]
    assert x.derivatives == [{'x': 13.85102, 'y': -0.1455}]
    assert x.formulas == ['cos(x)*y+13-x**2']

def test_guide(mocker):
    """
    todo
    """
    mocker.patch('builtins.input', side_effect=[2, 3, 5, '4*x+7*y'])
    x = AD()
    mocker.patch('builtins.input', side_effect=[2, 5, 8, 'sin(x)*7+4*tanh(y)'])
    x.guide()
    for li in x.derivatives:
        for key, value in li.items():
            li[key] = round(value, 5)
    assert x.inputs == {'y': 5.0, 'x': 8.0}
    assert [ round(elem, 5) for elem in x.outputs ] == [ round(elem, 5) for elem in [10.925144543414053] ]
    assert x.derivatives == [{'x': -1.0185, 'y': 0.00073}]
    assert x.formulas == ['sin(x)*7+4*tanh(y)']

def test_print(mocker):
    """
    """
    mocker.patch('builtins.input', side_effect=[2, 3, 5, '-x+3*(y)'])
    x = AD()
    print(x)
    assert x.__str__() == """
        Formula(s) saved: ['-x+3*(y)'],
        Value(s) used: {'y': 3.0, 'x': 5.0},
        Derivatives found: [{'x': -1, 'y': 3.0}]
        """
