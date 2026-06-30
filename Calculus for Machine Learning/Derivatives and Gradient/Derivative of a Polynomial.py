def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * x ** (n - 1)

result = poly_term_derivative(3, 2, 4)
print(result)