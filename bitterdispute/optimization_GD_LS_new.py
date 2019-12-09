#from variable import Variable
import numpy as np

def gradientDescent(f, init_val, lr=0.01, max_iters=10000, tol=1e-4):
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
    max_iters : integer, optional (default = 10000)
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
    if isinstance(init_val,list):
        num_vars = len(init_val)
        if num_vars > 1:
            iters = 0 # iteration counter
            init_stepsize = np.ones(num_vars) #define an inital difference between x and x0
            curr_x = np.asarray(init_val)
            tol_array= np.ones(num_vars)*tol
            for i in range(max_iters):
                prev_x = curr_x # Store current x value in prev_x
                curr_x = curr_x - lr * np.array(list(f(prev_x).der.values())) #Grad descent; needs to be updated
                init_stepsize = curr_x - prev_x # update the change in x
                iters = iters + 1 #update the values in iteration counter
                if init_stepsize.all() < tol_array.all():
                    return curr_x
                    break
            return ('reached maximum iterations')
        elif num_vars == 1:
            print("hello")
            iters = 0 # iteration counter
            init_stepsize = float('inf') #define an inital difference between x and x0
            curr_x = init_val[0]
            while (init_stepsize > tol and iters < max_iters):
                prev_x = curr_x # Store current x value in prev_x
                curr_x = curr_x - lr * np.array( list( f(curr_x).der.values() ) )[0] #Grad descent; needs to be updated
                init_stepsize = abs(curr_x - prev_x) # update the change in x
                iters+=1 #update the values in iteration counter
            return iters, curr_x
    else:
        raise TypeError("Please enter the initial values in a list.")
    #print("Total iterations", iters, "\n The local minimum occurs at", curr_x)  #Print iterations and the local minimum value

def f(val):
    x1 = Variable('x',val)
    f = (x1-5) ** 2
    return f
a = gradientDescent(f,init_val=[3])
print(a)

def f(val):
    x1 = Variable('x',val[0])
    x2 = Variable('y',val[1])
    f = (x1-5) ** 2 + (x2-5)**2
    return f
a = gradientDescent(f,init_val=[3,1])
print(a)


def backtrackingLineSearch(f, init_val, tau=0.01, c = 0.01, alpha = 10, max_iters=1000):
    """
    backtracking line search algorithm based on the Armijo–Goldstein condition, which finds the step size that provides a reasonable amount of improvement in the objective function.

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
        the step size which provides a reasonable amount of improvement in the objective function

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
    "Total iterations 9
    The alpha, step size, is 1.0000000000000002e-17"



    # when the initial guess is set to be closer to the minimum, the reasonable step size is getting smaller.
    """
    iters = 0
    init_val=np.array(init_val)
    fval1 = f(init_val).val # find the value at the initial guess
    fval2 = f(init_val + alpha).val # update the value
    if (fval1 - fval2) < 0:
        p=-1
    if (fval1 - fval2) > 0:
        p=1
    gradient = np.array(list(f(init_val).der.values())) #find the gradient
    m=(p*gradient).sum()
    t = -c * m
    while (fval1 - fval2) < (alpha * t):
        alpha = tau * alpha

        fval2 = f(init_val + alpha*p).val
        iters = iters+1
        # if (fval1 - fval2) >= (alpha * t).sum():
        #     return [iters, "hello", alpha]
        #     break
    print (iters, alpha)
    #print("Total iterations", iters, "\n The alpha, step size, is", alpha)

# def f(val):
#     x1 = Variable('x',val[0])
#     f = (x1-5) ** 2
#     return f
# a = backtrackingLineSearch(f, init_val=[7])
# b = backtrackingLineSearch(f, init_val=[5])
#
# def f(val):
#     x1 = Variable('x',val[0])
#     x2 = Variable('y',val[1])
#     f = (x1-5) ** 2 + (x2-5)**2
#     return f
# a = backtrackingLineSearch(f, init_val=[7,7])
# b = backtrackingLineSearch(f, init_val=[5,5])
