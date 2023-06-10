# Lagrangian Polynomial Interpolation

This repository provides three Python files that work together to solve problems related to function interpolation and estimating error bounds.

## File 1: lagrange_polynomials.py

This file contains the following functions:

### Function: lagrange_poly(p, xhat, n, x, tol)

The `lagrange_poly` function is used by functions in File 1. It evaluates the Lagrange polynomial using a given set of interpolation nodes and a tolerance.

### Function: deriv_lagrange_poly(p, xhat, n, x, tol)

The `deriv_lagrange_poly` function is used by the `approximate_derivative` function in File 1. It calculates the derivative of the Lagrange polynomial for a set of nodal points and evaluated points and checks for the distinctness of nodal points.

These functions work together to build reliable polynomial functions with small error bounds compared to the actual functions.

## File 2: compute_errors.py

This file contains the following functions:

### Function: interpolation_errors(a, b, n, P, f)

The `interpolation_errors` function calls the `poly_interpolation` function from File 1. It computes the maximum error, max{|p_p_j(x) - f(x)|}, in the domain [a, b] for a range of polynomial degrees P. The errors are calculated using a uniform set of interpolation nodes.

### Function: derivative_errors(x, P, m, H, n, f, fdiff)

The `derivative_errors` function calls the `approximate_derivative` function from File 1. It computes the error in approximating the derivative of a function at a given point for a range of polynomial degrees P and interval widths H.


Please feel free to adjust and customize the formatting as per your needs.

## File 3: approximations.py

This file contains the following functions:

### Function: poly_interpolation(a, b, p, n, x, f, produce_fig)

The `poly_interpolation` function calls the `lagrange_poly` function from File 3. It evaluates the pth order polynomial interpolation of a function f at a set of points x_j, where j ranges from 0 to n-1. The nodal interpolation points are uniformly spaced over the interval [a, b], including the endpoints. If `produce_fig` is True, the function plots the function f evaluated at the points x_j and the interpolant p_p(x) on the same axes.

### Function: poly_interpolation_2d(p, a, b, c, d, X, Y, n, m, f, produce_fig)

The `poly_interpolation_2d` function calls the `lagrange_poly` function from File 3. It evaluates the pth order polynomial p_p(x, y) of a function at a set of grid points stored in the m x n arrays X and Y. The components of the interpolant are uniformly spaced over the intervals [a, b] and [c, d] for x and y, respectively, including the endpoints. If `produce_fig` is True, the function produces a contour plot of the interpolant p_p(x).

### Function: approximate_derivative(x, p, h, k, f)

The `approximate_derivative` function calls the `deriv_lagrange_poly` function from File 3. It evaluates the derivative of the pth order polynomial interpolant of a function f at a point x. The interpolant points are equally spaced, and x coincides with one of the nodal points.

Feel free to adjust and customize the formatting as per your needs.


