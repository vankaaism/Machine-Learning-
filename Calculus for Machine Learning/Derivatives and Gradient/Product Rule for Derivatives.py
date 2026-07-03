import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    product = [0.0] * (len(f_coeffs) + len(g_coeffs) - 1)

    for i in range(len(f_coeffs)):
        for j in range(len(g_coeffs)):
            product[i + j] += f_coeffs[i] * g_coeffs[j]

    derivative = []

    for power in range(1, len(product)):
        derivative.append(round(product[power] * power, 4))


    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    if not derivative:
        return [0.0]

    return derivative
    pass

f = [1, 2]      # f(x) = 1 + 2x
g = [3, 4]      # g(x) = 3 + 4x

result = product_rule_derivative(f, g)
print(result)