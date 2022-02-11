import numpy as np
import sympy as sym

#Define our functions of interest in form f(x,y) = 0
X, Y = sym.symbols('X Y', real = True)
F = X*sym.cos(Y) + Y*sym.sin(X) + 1
G = X**2 + Y**2 - 4

#takes initial values, number of iterates, and functions of interest
def newton_raphson(x0,y0,n,f,g):
    #forms jacobian using partial differentiation
    jacobian = sym.Matrix([[sym.diff(f,X), sym.diff(f,Y)],[sym.diff(g,X), sym.diff(g,Y)]])
    try:
        inverse_jacobian = jacobian ** -1
    except sym.det(jacobian) == 0:
        raise TypeError('The matrix doesn\'t have an inverse')
    #forms the matrices for the initial solution and functions
    function_and_inv_jacobian = inverse_jacobian * sym.Matrix([[f],[g]])
    lambdify_function_and_inv_jacobian = sym.lambdify([X,Y], function_and_inv_jacobian, modules = 'sympy')
    previous_solution = sym.Matrix([[x0],[y0]])
    print('Our 1st iterates are {}'.format(previous_solution))
    #the actual method
    for i in range(n):
        next_solution = previous_solution - lambdify_function_and_inv_jacobian(previous_solution[0],previous_solution[1])
        previous_solution = next_solution
        print('Our {}th iterates are {}'.format(i+2, previous_solution))


newton_raphson(-1.0,1.0,500,F,G)








