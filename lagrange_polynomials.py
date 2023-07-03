#################################################################
## Functions to compute Lagrange polynomials
#################################################################

#################################################################
## Imports
## - No further imports should be necessary
#################################################################
import numpy as np
#################################################################

#################################################################
## Functions to be completed by student
#################################################################

#%% Q1 code
def lagrange_poly(p,xhat,n,x,tol):

    """
    Evaluates at the points x, the p+1 Lagrange polynomial associated with the 
    nodal/interpolating points xhat.

    Parameters
    ----------
    p : int
          polynomial degree to use (assumed positive)
    xhat : numpy.ndarray of shape (p+1,)
          nodal points upon which the Lagrange polynomials are defined
    n : int/integer array
          number of points at which to evaluate the interpolant
          if n is int, n0=n, else n0 = n[0],n1 = n[1],etc
    x : numpy.ndarray of shape (n0,n1,...)
          points at which to evaluate the interpolant
    tol : float
          tolerance for which floating point numbers x and y are 
          considered equal: |x-y| < tol

    Returns
    -------
    lagrange_matrix : numpy.ndarray of shape (p+1,n0,n1,...)
        Matrix of evaluated Lagrange polynomial
    error_flag :: int
        0 - points are distinct, 1 - points are not distinct (error)

    Examples
    --------
    >>> lagrange_matrix, error_flag = lagrange_poly(3,np.array([-1,0,1,2]),5,np.linspace(5),1.0e-10)
    """

    #Check xhat is of the correct length
    #Note, this is good practice
    if xhat.shape != (p+1,):
        return None, None #Premature exit

    l_matrix_shape = np.concatenate(([p+1],x.shape))
    lagrange_matrix = np.ones(l_matrix_shape) #Preallocate for speed
    error_flag = 0 #Initially we have no error

    #Build up the polynomials one term at a time
    for k, xhat_k in enumerate(xhat):
        for m, xhat_m in enumerate(xhat):
            if m != k: #Make sure we don't divide by zero
                if np.abs(xhat_k-xhat_m) < tol: #Nodes regarded as equal
                    error_flag = 1
                    return lagrange_matrix, error_flag #immediate return of function
                
                lagrange_matrix[k] *= (x-xhat_m)/(xhat_k-xhat_m) #Update lagrange matrix

    return lagrange_matrix, error_flag

#%% Q5 Code
def deriv_lagrange_poly(p,xhat,n,x,tol):

    if xhat.shape != (p+1,):
        return None,None
    deriv_lagrange_matrix = np.zeros(np.concatenate(([p+1],x.shape)))
    error_flag = 0
    
    for i,xhat_i in enumerate(xhat):
        total = 0
        
        for j,xhat_j in enumerate(xhat):
            #Makes sure not dividing by 0
            if j != i:
                if abs(xhat_i - xhat_j) < tol:
                    error_flag = 1
                    return deriv_lagrange_matrix, error_flag
  #The algorithm is specifically for the derivative of lagrange polynomial         
                prod = 1/(xhat_i - xhat_j)
                for k,xhat_k in enumerate(xhat):
                    #Makes sure not dividing by 0
                    if (k != i and k != j): 
                        prod *= (x-xhat_k)/(xhat_i - xhat_k)
                total = prod + total
        deriv_lagrange_matrix[i] += total
    return deriv_lagrange_matrix, error_flag

#################################################################
## Test Code ##
#################################################################
#%% Q1 Test
################

# Initialise
p = 3
xhat = np.linspace(0.5,1.5,p+1)
n = 7
x = np.linspace(0,2,n)
tol = 1.0e-10
#Run the function
lagrange_matrix, error_flag = lagrange_poly(p,xhat,n,x,tol)

print("\n################################")
print("Q1 TEST OUTPUT:\n")
print("lagrange_matrix =\n")
print(lagrange_matrix)
print("")
print("error_flag = " + str(error_flag))

################
#%% Q5 Test
################

# Initialise

p = 3
xhat = np.linspace(-0.5,0.5,p+1)
n = 6
x = np.linspace(-1,1,n)
tol = 1.0e-12
#Run the function
deriv_lagrange_matrix, error_flag = deriv_lagrange_poly(p,xhat,n,x,tol)

print("\n################################")
print("Q5 TEST OUTPUT:\n")
print("deriv_lagrange_matrix =\n")
print(deriv_lagrange_matrix)
print("")
print("error_flag = " + str(error_flag))
