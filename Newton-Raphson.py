import sympy as sym

#Define our functions of interest in form f(x,y) = 0
X, Y = sym.symbols('X Y', real = True)
F = Y - X**3 + 1
G = Y**3 - X + 1

#takes initial values, number of iterates, and functions of interest
def newton_raphson(x0,y0,n,f,g):
    #forms jacobian using partial differentiation
    jacobian = sym.Matrix([[sym.diff(f,X), sym.diff(f,Y)], [sym.diff(g,X), sym.diff(g,Y)]])
    try:
        inverse_jacobian = jacobian ** -1
    except jacobian.det() == 0:
        raise TypeError('The matrix doesn\'t have an inverse')
    #forms the matrices for the initial solution and functions
    function_matrix = sym.Matrix([[f],[g]])
    previous_solution = sym.Matrix([[x0],[y0]])
    print('Our 1st iterates are {}'.format(previous_solution))
    #the actual method, it is very slow for sym functions but works very well for polynomials 
    for i in range(n):
        next_solution = previous_solution - (inverse_jacobian * function_matrix).subs({X:previous_solution[0],Y:previous_solution[1]})
        print('Our {}th iterates are {}'.format(i+2, next_solution.evalf()))
        previous_solution = next_solution
    

newton_raphson(1,0.5,5,F,G)








