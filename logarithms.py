def natural_log(x):
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers.")
    result = 0
    n = 1000000
    for i in range(1, n + 1):
        result += (1 / i) * ((x - 1) ** i) / (x ** i)
    return result
