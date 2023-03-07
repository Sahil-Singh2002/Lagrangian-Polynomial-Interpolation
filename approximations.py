#################################################################
## Functions to find a range of approximations using polynomials
#################################################################

#################################################################
## Imports
## - No further imports should be necessary
## - If you wish to import a non-standard modules, ask Ed if that 
## - is acceptable
#################################################################
import numpy as np
import matplotlib.pyplot as plt
import lagrange_polynomials as lp #previously written functions
#################################################################


#################################################################
## Functions to be completed by student
#################################################################

#%% Q2 code
def poly_interpolation(a,b,p,n,x,f,produce_fig):

    #Example of creating a figure object
    
    xhat = np.linspace(a,b,p+1)
    tol = 1.0e-10
    interpolant = 0
    
    for j in range(p+1):
        term = lp.lagrange_poly(p,xhat,n,x,tol)[0][j]*f(xhat[j])
        interpolant += term
    
    if produce_fig == True:
    
        fig,ax = plt.subplots() #This line is required
    
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        
        ax.plot(x,interpolant,"s",label="$p_p(x)$",linestyle=" ")
        ax.plot(x,f(x),"o",label="$f(x)$",linestyle=":")
        ax.legend()
        
    elif produce_fig == False:
        fig = None
    #Remove the following line when you have completed the code  

    return interpolant, fig

#%% Q4 code
def poly_interpolation_2d(p,a,b,c,d,X,Y,n,m,f,produce_fig):
   
    xhat = np.linspace(a,b,p+1)
    yhat = np.linspace(c,d,p+1)
    tol = 1.0e-10
    interpolant = 0
#Algorithem to Plot the 2D polynomial interpolation    
    for j in range(p+1):
        for i in range(p+1):
            term = lp.lagrange_poly(p,xhat,n,X,tol)[0][j]*f(xhat[j],yhat[i])*lp.lagrange_poly(p,yhat,n,Y,tol)[0][i]
            interpolant += term
    if produce_fig == True:
#This line is required
        fig = plt.figure() 
        ax = fig.add_subplot(111,aspect = "equal")
#Plots Contour          
        cs = ax.contour(X,Y,interpolant)
        ax.clabel(cs)
#Plots Labels       
        ax.set_xlabel("$ X axies$")
        ax.set_ylabel("$Y axies$")
        ax.set_title("$Level curve of p_p (x) $")

    elif produce_fig == False:
        fig = None

    return interpolant,fig  



#%%Q6#~ code
def approximate_derivative(x,p,h,k,f):
#Algorith built to compute a uniformly spaced linspace of xhat with 
#equal distance of h   
    tol = 1.0e-10
    x_int = np.arange(1) +x
    xhat_i = np.arange(p+1)
    xhat_i = xhat_i * h
    xhat_i = xhat_i +(x-k*h)
#Constanst    
    n,term,j = 1,0,0   
#array of the derivative lagrange polynomial, used in the sum
    d_lag_p = lp.deriv_lagrange_poly(p,xhat_i,n,x_int,tol)[0]
    
    for i in d_lag_p :
        term = i[0]*f(xhat_i[j]) + term
        j= j+1
        deriv_approx = term

    return deriv_approx
#################################################################
## Test Code ##
## You are highly encouraged to write your own tests as well,
## but these should be written in a separate file
#################################################################
print("\nAny outputs above this line are due to importing lagrange_polynomials.py.\n")

################
#%% Q2 Test
################

# Initialise
a = 0.5
b = 1.5
p = 3
n = 10
x = np.linspace(0.5,1.5,n)
f = lambda x: np.exp(x)+np.sin(np.pi*x)
#Run the function
interpolant, fig = poly_interpolation(a,b,p,n,x,f,True)

print("\n################################")
print('Q2 TEST OUTPUT:\n')
print("interpolant = \n")
print(interpolant)

################
#%% Q4 Test
################

f = lambda x,y : np.exp(x**2+y**2)
n = 4; m = 3
a = 0; b = 1; c = -1; d = 1 
x = np.linspace(a,b,n)
y = np.linspace(c,d,m)
X,Y = np.meshgrid(x,y)

interpolant,fig = poly_interpolation_2d(11,a,b,c,d,X,Y,n,m,f,True)

print("\n################################")
print('Q4 TEST OUTPUT:\n')
print("interpolant = \n")
print(interpolant)

################
#%% Q6 Test
################

print("\n################################")
print("Q6 TEST OUTPUT:\n")
#Initialise
p = 3
h = 0.1
x = 0.5
f = lambda x: np.cos(np.pi*x)+x

for k in range(4):
    #Run test 
    deriv_approx = approximate_derivative(x,p,h,k,f)
    print("k = " + str(k)+ ", deriv_approx = " + str(deriv_approx))