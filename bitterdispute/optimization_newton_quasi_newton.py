
from elementary_functions import *
from variable import Variable

import numpy as np
import matplotlib.pyplot as plt


def hessian(f, x, dx=1e-5):
    '''
    Creates a function that computes the hessian matrix of a scalar field.
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
    
def help_Quasi_Newton(f, x0, B, h=0.1):
    ## DFP
    x = np.array(x0).ravel()
    #H = hessian(f, x0)
    #B = np.linalg.inv(H)
        
    # Updates x        
    dfx = np.array(list(f(x0).der.values())) # df(x0) #
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


def help_Newton(f, x0, h=0.1, stop_stepsize=1e-6):
    
    x = np.array(x0).ravel()
    H = hessian(f, x0)#f(x0).der2
    
    # Updates x        
    dfx = np.array(list(f(x0).der.values())) # df(x0) #
    step = np.linalg.solve(H, -dfx)
    
    if np.isscalar(x0):
        dfx = dfx[0]
    
    if np.linalg.norm(step, ord=2) > stop_stepsize: 
        if np.isscalar(x0):
            step = step[0]
        
        dx = step*h 
        
        x = x + np.array(dx)   
    
    if np.isscalar(x0):
        return x[0]
    else:
        return x
    
def plot_opt(x_ls, f_=lambda x: (x-5)**2):
    x_ls = np.array(x_ls)

    y = f_(x_ls)

    x_ = np.linspace(-2, 2, 250)
    z_ = f_(x_)

    plt.plot(x_ls, y, lw=3, alpha=0.5, label="Optimization")
    plt.plot(x_, z_, lw=3, ls="--", alpha = 0.5, label="Real")
    plt.scatter(x_ls[-1], y[-1], color="red", s=10,label="End")
    #plt.xlim(-2-10, 2+10)
    #plt.ylim(min(z_)-10, max(z_)+10)
    plt.legend()
    plt.show()
    
def Quasi_Newton(f, x0, iter_max=100, error_max=1e-5):
    xn = x0
    x_ls = [xn]
    H = hessian(f, x0)
    B = np.linalg.inv(H)
    
    for i in range(iter_max):
        x_new, B = help_Quasi_Newton(f=f, x0=xn, B=B)
        
        if np.mean(abs(x_new-xn))<error_max:
            print("Reach error requirement. At iteration {}".format(i))
            return xn, x_ls
        
        x_ls.append(xn)
        xn = x_new
        
    print("Reach max iteration!")
    print("Result:", xn, "; f(x) = ", funct(xn).val)
    
    return xn, x_ls

def Newton(f, x0, iter_max=100, error_max=1e-5):
    xn = x0
    x_ls = [xn]
    for i in range(iter_max):
        x_new = help_Newton(f=f, x0=xn)
        
        if np.mean(abs(x_new-xn))<error_max:
            print("Reach error requirement. At iteration {}".format(i))
            return xn, x_ls
        
        x_ls.append(xn)
        xn = x_new
        
    print("Reach max iteration!")
    print("Result:", xn, "; f(x) = ", funct(xn).val)
    
    return xn, x_ls