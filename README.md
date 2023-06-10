# Lagrangian Polynomial Interpolation

This repository provides three Python files that work together to solve problems related to function interpolation and estimating error bounds.

$$\textbf{Lagrange Polynomial Interpolation}$$

$$
L_i(x) = \prod_{j=0, j \neq i}^{p} \frac{(x - \hat{x}_j)}{(\hat{x}_i - \hat{x}_j)}
$$

A function $f : \mathbb{R} \rightarrow \mathbb{R}$ can then be interpolated by the $p$th order polynomial function $p_p(x)$ given by:

$$
p_p(x) = \sum_{i=0}^{p} f(\hat{x}_i) L_i(x)
$$


## lagrange_polynomials.py

This file contains functions for evaluating Lagrange polynomials and approximating derivatives using interpolation.

- `lagrange_poly(p, xhat, n, x, tol)`: Evaluates the Lagrange polynomial using a given set of interpolation nodes and a tolerance.
- `deriv_lagrange_poly(p, xhat, n, x, tol)`: Approximates the derivative of a function at a given point using Lagrange interpolation.

## compute_errors.py

This file contains functions for computing interpolation errors and derivative errors.

- `interpolation_errors(a, b, n, P, f)`: Computes the maximum interpolation error in the domain [a, b] for a range of polynomial degrees P.
- `derivative_errors(x, P, m, H, n, f, fdiff)`: Computes the error in approximating the derivative of a function at a given point for a range of polynomial degrees P and interval widths H.

## approximations.py

This file contains functions for polynomial interpolation and approximation in both 1D and 2D.

- `poly_interpolation(a, b, p, n, x, f, produce_fig)`: Evaluates the pth order polynomial interpolation of a function f at a set of points x_j in the interval [a, b].
- `poly_interpolation_2d(p, a, b, c, d, X, Y, n, m, f, produce_fig)`: Evaluates the pth order polynomial interpolation of a function f on a 2D grid.
- `approximate_derivative(x, p, h, k, f)`: Approximates the derivative of a function at a given point using polynomial interpolation.

## Conclusion

This repository provides Python files for Lagrange Polynomial Interpolation and error estimation. The lagrange_polynomials.py file includes functions for evaluating Lagrange polynomials and their derivatives. The compute_errors.py file computes interpolation errors and derivative errors. The approximations.py file handles polynomial interpolation and approximation in both 1D and 2D. These files work together to perform accurate function interpolation and estimate error bounds. By leveraging the Lagrange interpolation method, users can approximate functions and derivatives with high precision. The repository is a valuable resource for numerical analysis and scientific computing tasks.
