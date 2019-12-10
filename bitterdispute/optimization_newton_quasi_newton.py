
from bitterdispute.elementary_functions import *
from bitterdispute.variable import Variable

import numpy as np


def hessian(f, x, dx=1e-6):
    '''
    Creates a function that computes the hessian matrix of a scalar field.
    
    Parameters
    ----------
    f : callable function object
        A differentiable real-valued function
    x:  list of float contains value of variables
    dx: float, step length.
   
    Returns
    -------
    Hessian:
        Hessian matrix for the input function f
        
    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
        ...     f = (x1-5) ** 2
	...     return f
	>>> a = hessian(f, 1)
	>>> print(a)
	"[[0.5000444502911705]]"
    '''
    if np.isscalar(x):
#         H = f(x).der2
#         return [[H]]
        x = float(x)
        return [[(f(x+dx).val - 2.*f(x).val + f(x-dx).val) / (4.*dx*dx)]]
    else:
        n = x.size
        hf = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                xll = np.array(x)
                xll[i] = xll[i] - dx
                xll[j] = xll[j] - dx
                xul = np.array(x)
                xul[i] = xul[i] - dx
                xul[j] = xul[j] + dx
                xlr = np.array(x)
                xlr[i] = xlr[i] + dx
                xlr[j] = xlr[j] - dx
                xur = np.array(x)
                xur[i] = xur[i] + dx
                xur[j] = xur[j] + dx
                hf[i, j] = (f(xur).val - f(xlr).val - f(xul).val + f(xll).val) / (4.*dx*dx)
        return hf

def help_Quasi_Newton(f, x0, B, h=0.09):
    '''
    help function to calcuate quasi newton 
    
    Parameters
    ----------
    f : callable function object
        A differentiable real-valued function
    x0: list of float contains initial guess of roots
    B : the inverse of hessian matrix
    h : float (default = 0.09) The learning rate.
        
    Returns
    -------
    xn: updated roots guess
    B : approximate of matrix B
    
    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
        ...     f = (x1-5) ** 2
	...     return f
    >>> H = hessian(f, x0)
    >>> B = np.linalg.inv(H)
	>>> xn, B = help_Quasi_Newton(f, x0, B)
	>>> xn, B
	(2.599857771712432, array([[0.5]]))
    '''
    ## DFP
    x = np.array(x0).ravel()
    #H = hessian(f, x0)
    #B = np.linalg.inv(H)

    # Updates x
    dfx = np.array([f(x0).der.get(key) for key in sorted(f(x0).der)]) # df(x0) #list(f(x0).der.values())

    if np.isscalar(x0):
        dfx = dfx[0]
    dx = - h * np.dot(B, dfx)

    xn = x + dx

    # Updates B
    y = np.array(list(f(xn).der.values()))
    if np.isscalar(x0):
        y = y[0]
    y = y - dfx

    By = np.dot(B, y)
    dB = np.outer(dx, dx) / np.dot(y, dx) - np.outer(By, By) / np.dot(y, By)
    B += dB

    if np.isscalar(x0):
        return xn[0][0], B
    else:
        return xn, B


def help_Newton(f, x0, h=0.1):
    '''
    help function to calcuate newton 
    
    Parameters
    ----------
    f : callable function object
        A differentiable real-valued function
    x0: list of float contains initial guess of roots
    h : float (default = 0.09) The learning rate.
        
    Returns
    -------
    xn: updated roots guess
    
    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
        ...     f = (x1-5) ** 2
	...     return f
	>>> xn = help_Newton(f, x0)
	>>> xn
	2.599857771712432
    '''
    x = np.array(x0).ravel()
    H = hessian(f, x0)#f(x0).der2
    B = np.linalg.pinv(H)

    # Updates x
    dfx = np.array([f(x0).der.get(key) for key in sorted(f(x0).der)]) # df(x0) #list(f(x0).der.values())
    if np.isscalar(x0):
        dfx = dfx[0]

    dx = -np.dot(B, dfx)*h

    xn = x + np.array(dx)

    if np.isscalar(x0):
        return xn[0][0]
    else:
        return xn


def Quasi_Newton(f, x0, iter_max=100, error_max=1e-10):
    '''
    function to calcuate quasi newton in DFP
    
    Parameters
    ----------
    f        : callable function object
               A differentiable real-valued function
    x0       : list of float contains initial guess of roots
    iter_max : integer, optional (default = 100)
               The maximum number of iterations to run
    error_max: float, optional (default = 1e-10)
               This tells us when to stop the algorithm
        
    Returns
    -------
    xn   : optimal roots guess
    x_ls : historical guss of xn
    
    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
        ...     f = (x1-5) ** 2
	...     return f
	>>> xn, x_ls = Quasi_Newton(f, x0)
	Reach max iteration!
    Result: 4.9999291654054305 ; f(x) =  5.017539787821024e-09
    '''
    xn = x0
    x_ls = [xn]
    H = hessian(f, x0)
    B = np.linalg.inv(H)

    for i in range(iter_max):
        x_new, B = help_Quasi_Newton(f=f, x0=xn, B=B)

        if np.mean(abs(x_new-xn))<error_max:
            print("Reach requirement. At iteration {}".format(i))
            return xn, x_ls

        x_ls.append(xn)
        xn = x_new

    print("Reach max iteration!")
    print("Result:", xn, "; f(x) = ", f(xn).val)

    return xn, x_ls

def Newton(f, x0, iter_max=100, error_max=1e-6):
    '''
    help function to calcuate newton 
    
    Parameters
    ----------
    f        : callable function object
               A differentiable real-valued function
    x0       : list of float contains initial guess of roots
    iter_max : integer, optional (default = 100)
               The maximum number of iterations to run
    error_max: float, optional (default = 1e-10)
               This tells us when to stop the algorithm
        
    Returns
    -------
    xn   : optimal roots guess
    x_ls : historical guss of xn
    
    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
        ...     f = (x1-5) ** 2
	...     return f
	>>> xn = Newton(f, x0)
	>>> xn
	Reach requirement. At iteration 28
    4.999997543564156
    '''
    xn = x0
    x_ls = [xn]
    for i in range(iter_max):
        x_new = help_Newton(f=f, x0=xn)

        if np.mean(abs(x_new-xn))<error_max:
            print("Reach requirement. At iteration {}".format(i))
            return xn, x_ls

        x_ls.append(xn)
        xn = x_new

    print("Reach max iteration!")
    print("Result:", xn, "; f(x) = ", f(xn).val)

    return xn, x_ls
