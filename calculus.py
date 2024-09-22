def derivative(func, x, h=1e-5):
    return (func(x + h) - func(x)) / h

def definite_integral(func, a, b, n=1000):
    width = (b - a) / n
    total = 0
    for i in range(n):
        total += func(a + i * width) * width
    return total

def indefinite_integral(func):
    return "Indefinite integral not supported without specific function."
