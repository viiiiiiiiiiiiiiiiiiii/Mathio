def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    guess = x / 2.0
    for _ in range(10):
        guess = (guess + x / guess) / 2.0
    return guess

def cube_root(x):
    if x < 0:
        return -(-x) ** (1/3)
    return x ** (1/3)
