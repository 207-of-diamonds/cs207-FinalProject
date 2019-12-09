from scalar import Scalar
import numpy as np

def gradientDescent(f, init_val, lr=0.01, max_iters=1000, tol=1e-4):
    '''
    Minimize a function using gradient descent.

    Parameters
    ----------
    f : callable function object
        A differentiable real-valued function
    init_val: list of float
        contains initial guess of roots
    lr: float (default = 0.01)
        The learning rate.
    max_iters : integer, optional (default = 1000)
        The maximum number of iterations to run
    tol: float, optional (default = 1e-10)
        This tells us when to stop the algorithm
    data: numpy.ndarray (m x n), optional (default = [])

    Returns
    -------
    minimum:
        variable values corresponding to the minimum value of f
        contains the optimal scalar solution and the derivative at that point

    EXAMPLES
	=========
	>>> def f(val):
	...     x1 = Scalar(val)
    ...     f = (x1-5) ** 2
	...     return f
	>>> a = gradientDescent(f)
	>>> print(a)
	"Total iterations 298
    The local minimum occurs at 4.99514263709298"
    '''
	#num_vars = len(init_val) # Number of variables
    iters = 0 # iteration counter
    init_stepsize = float('inf') #define an inital difference between x and x0
    curr_x = init_val
    while (init_stepsize > tol and iters < max_iters):
            prev_x = curr_x # Store current x value in prev_x
            curr_x = curr_x - lr * f(prev_x).der #Grad descent; needs to be updated
            init_stepsize = abs(curr_x - prev_x) # update the change in x
            iters = iters+1 #update the values in iteration counter

    print("Total iterations", iters, "\n The local minimum occurs at", curr_x)  #Print iterations and the local minimum value

# def f(val):
#     x1 = Scalar(val)
#     #x2 = Scalar(values)
#     f = (x1-5) ** 2 #+ x2
#     return f
# a = gradientDescent(f,init_val=3)


def backtrackingLineSearch(f, init_val, tau=0.1, c = 0.1, alpha = 1):
    """
    backtracking line search algorithm based on the Armijo–Goldstein condition,
    which finds the step size that provides a reasonable amount of improvement
    in the objective function.

    INPUTS
    =======
    f: callable function object
        A differentiable real-valued function
    init_val: list of int or float
        contains initial value of variables
    tau: float, optional (default = 0.1)
        a selected control parameter; 0 < tau < 1
    c: float, optional (default = 0.1)
        a selected control parameter; 0 < c < 1
    alpha:float, optional (default = 1)
        initial alpha, the parameter that will need to be updated.

    RETURNS
    ========
    alpha:
        the step size which provides a reasonable amount of improvement
        in the objective function

    EXAMPLES
    =========
    >>> def f(val):
    ...     x1 = Scalar(val)
    ...     f = (x1-5) ** 2
    ...     return f

    >>> a = backtrackingLineSearch(f, init_val=6)
    "Total iterations 1
    The alpha, step size, is 0.1"
    >>> b = backtrackingLineSearch(f, init_val=5)
    "Total iterations 16
    The alpha, step size, is 1.000000000000001e-16"
    >>> c = backtrackingLineSearch(f, init_val=1)
    "Total iterations 0
    The alpha, step size, is 1"

    # when the initial guess is set to be closer to the minimum,
    the reasonable step size is getting smaller.
    """
    iters = 0
    fval1 = f(init_val).val # find the value at the initial guess
    fval2 = f(init_val + alpha).val # update the value
    if (fval1 - fval2) < 0:
        p=-1
    if (fval1 - fval2) > 0:
        p=1
    gradient = f(init_val).der #find the gradient
    m = f(init_val).der #
    t = -c * m
    while (fval1 - fval2) < alpha * t:
        alpha = tau * alpha
        fval2 = f(init_val + alpha*p).val
        iters = iters+1
        print (fval1 - fval2, alpha * t)
    print("Total iterations", iters, "\n The alpha, step size, is", alpha)

# def f(val):
#     x1 = Scalar(val)
#     f = (x1-5) ** 2
#     return f
# a = backtrackingLineSearch(f, init_val=6)
# b = backtrackingLineSearch(f, init_val=5)
# c = backtrackingLineSearch(f, init_val=1)
