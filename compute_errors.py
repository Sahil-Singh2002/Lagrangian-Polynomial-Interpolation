#################################################################
## Functions to compute some approximation errors
#################################################################

#################################################################
## Imports
## - No further imports should be necessary
## - If you wish to import a non-standard modules, ask Ed if that 
## - is acceptable
#################################################################
import numpy as np
import matplotlib.pyplot as plt
import approximations as approx #import previously written functions
#################################################################

#################################################################
## Functions to be completed by student
#################################################################

#%% Q3 code
def interpolation_errors(a,b,n,P,f):
    """
    Computes (approximations to), the error max|p_p_j(x) -f(x)| with the domain
    of x in between closed interval of a to b. For a range of polynomial degrees P = {p_j} from j = 0 to n-1. 
    
    Parameters
    ----------
    a : float
          The begining value of our intervel.
         
    b : float
          The end value of our intervel.
          
    n : int/integer array
          Number of points at which to evaluate the interpolant
          
    P : int/integer array
          The degree of the polynomial
          
    f : function
          The function is any anyltical function for which we want the 
          polynomial interpolation for.
          
    Returns
    -------
    error_matrix : numpy.ndarray of shape (n,)
        Matrix of 
    fig :: matplotlib.figure.Figure
        plots the error_matrix against the Polynomial Degrees P = {p_j} 
        where j is ranging from the values of 0 to n-1
        

    Examples
    --------
    >>> when P = {1,2,3,...,10} It will plot the for that number of error matrix elements.
    Case A. 
            error_matrix, fig = interpolation_errors(0,1,10,P,lambda x: exp{2x})
            Produces a linearly decreasing line which showes 
            higher the Degree of polynomial interpolent the greater our accuracy would be.
            
    Case B. 
            error_matrix, fig = interpolation_errors(-5,5,10,P,lambda x: 1/(1+25x^2) )
            This produces a non-linear plot where it shows multiple spikes in the error 
            such as at point p_8 and p_10 but the lowest error we see at p_4 showing
            the polynomial interpolent 4 is where highest accuray.
    """
    #Remove the following two lines when you have completed the code
    x = np.linspace(a,b,2000)
    
    list_of_error = []
    
    for k in P:
        interpolant, fig = approx.poly_interpolation(a,b,k,2000,x,f,False)
        e = interpolant - f(x)
        list_of_error.append(max(abs(e)))
    error_matrix = np.array(list_of_error)
    
    fig,ax = plt.subplots()
    ax.set_xlabel("${p_k}$")
    ax.set_ylabel("$max{|p_k- f(x) |}$")
    
    plt.semilogy(P,error_matrix)
    plt.show()
    
    
    
    return error_matrix, fig
#%% Q7 code 
def derivative_errors(x,P,m,H,n,f,fdiff):
    """
     The function uses a set of m even polynomial degrees and a set of n width H 
     to return (m x n) Matrix E, which is our derivitive apromixmation Error.
    
    Parameters
    ----------
    x : float
        The point at which we want to approximate the error between 
        our derivitive lagrange polynomial interpolant and actual derivitive 
        function.      
    m : int/integer array
        Number of Polynomial degrees which would be examined    
    H : Array
        A set of n width H = {h_j} with j ranging from 0 to n-1.
    n : int/integer array
        Number of points at which to evaluate the interpolant    
    P : Array
        The degree of the polynomial, a set of even polynomial P = {p_i} with i ranging from 0 to m-1.  
    f : function
        The function is any anyltical function for which we want the 
        polynomial interpolation for.
    fdiff : function
        The function is any anyltical function for which we want the 
        derivitive polynomial interpolation for.
          
    Returns
    -------
    E : numpy.ndarray of shape (m,n)
        Matrix of E[i][i] = | f'(x) - p'_(p_j,h_j) (x) | the error between 
        the derivitive interpolant and actual derivitive function.
    fig :: matplotlib.figure.Figure
        The plot of {E_ij} j ranging from 0 to n-1 for each p_i. With both x and y axes
        in the form of logarithmic scale.
       
    Examples
    --------
    >>> P = np.array([2,4,6,8])
        H = np.array([1/4,1/8,1/16,1/32,1/64,1/128,1/256])

        n,m = 7,4

        Case A. f(x) = exp{2x} for x = 1
        
        The Error is increasing linearly for all the interpolant for H, We see then that for the 
        first 3 P values it looks to be decreasing as the value of the interval is reduced.
        However for the last element of H, it is not quite linear as the lowest point of error 
        for this is between 10^-2 and 10^-1. So as the approximation is more accurate for higher 
        interpolant with a reasonable interval width. As seen on the graph

        Case B. f(x) = {0 ,for x<= 0 and x^2 ,for x>0
        
        We see the difference in our error for the interpolant is decreasing. However Error increases
        in a linear way for each of the interpolant as the value in H increases. This implies a 
        more reliable for higher interpolant. As seen on the graph.                                      
    """
    




# Initualises the value of E for use to be a matrix with dimension (m x n)
# to be a null matrix
    E = np.zeros([m,n])
# double forloop tp create the derivative errors |f'(x) - p'_p(i),h(j)|=E_(i,j)
    for i,p in enumerate(P):
        for j,h in enumerate(H):
            e = approx.approximate_derivative(x,p,h,p/2,f) - fdiff(x)
            E[i][j] += abs(e)    
#Plot
    #set the scale for both x and y axies to be in log
    fig = plt.figure()
    plt.xscale("log")
    plt.yscale("log")
    #Label the axies
    plt.xlabel("$H = {h_j}$")
    plt.ylabel("Error in log")   
    #Graph
    for i,p in enumerate(P):
        plt.plot(H,E[i])
    return E, fig

#################################################################
## Test Code ##
## You are highly encouraged to write your own tests as well,
## but these should be written in a separate file
#################################################################
print("\nAny outputs above this line are due to importing approximations.py.\n")

################
#%% Q3 Test
################

# Initialise
n = 5
P = np.arange(1,n+1)
a = -1
b = 1
f = lambda x: 1/(x+2)

#Run the function
error_matrix, fig = interpolation_errors(a,b,n,P,f)

print("\n################################")
print('Q3 TEST OUTPUT:\n')

print("error_matrix = \n")
print(error_matrix)

################
#%% Q7 Test
################

#Initialise
P = np.array([2,4,6])
H = np.array([1/4,1/8,1/16])
x = 0
f = lambda x: 1/(x+2)
fdiff = lambda x: -1/((x+2)**2)

#Run the function
E, fig = derivative_errors(x,P,3,H,3,f,fdiff)

print("\n################################")
print("Q7 TEST OUTPUT:\n")

print("E = \n")
print(E)
plt.show()

