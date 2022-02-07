import numpy as np
import sympy as sym

#Define our functions of interest in form f(x,y) = 0
X, Y = sym.symbols('X Y', real = True)
F = X**3 - Y - 1
G = X - Y**3 - 1

#takes initial values, number of iterates, and functions of interest
def newton_raphson(x0,y0,n,f,g):
    #forms jacobian using partial differentiation
    jacobian = sym.Matrix([[sym.diff(f,X), sym.diff(f,Y)], [sym.diff(g,X), sym.diff(g,Y)]])
    try:
        inverse_jacobian = jacobian ** -1
    except jacobian.det() == 0:
        raise TypeError('The matrix doesn\'t have an inverse')
    funciton_matrix = sym.Matrix([[f],[g]])
    for i in range(n):
        next_solution = previous_solution - (inverse_jacobian*
        
        print(inverse_jacobian.subs({X:5,Y:2}))



newton_raphson(0,0,5,F,G)








