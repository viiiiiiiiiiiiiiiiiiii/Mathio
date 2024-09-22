# Usage Documentation

This document provides detailed examples of how to use each function in the Mathio library.

## Basic Operations

```python
import mathio

result = mathio.add(10, 5)  # 15
result = mathio.subtract(10, 5)  # 5
result = mathio.multiply(10, 5)  # 50
result = mathio.divide(10, 5)  # 2
```

## Trigonometry

```python
result = mathio.sin(1.5708)  # ~1.0
result = mathio.cos(3.14159)  # ~-1.0
result = mathio.tan(0)  # 0.0
```

## Roots

```python
result = mathio.square_root(9)  # 3.0
result = mathio.cube_root(27)  # 3.0
```

## Logarithms

```python
result = mathio.natural_log(2.71828)  # ~1.0
```

## Algebra

```python
result = mathio.solve_linear_equations(2, -4)  # 2.0
result = mathio.quadratic_formula(1, -3, 2)  # (2.0, 1.0)
```

## Calculus

```python
def func(x):
    return x**2
derivative = mathio.derivative(func, 3)  # 6.0
integral = mathio.definite_integral(func, 0, 2)  # 2.66667
```

## Statistics

```python
data = [1, 2, 3, 4, 5, 5]
mean = mathio.mean(data)  # 3.3333
median = mathio.median(data)  # 3.5
mode = mathio.mode(data)  # 5
stdev = mathio.standard_deviation(data)  # 1.29099
```

## Geometry

```python
result = mathio.area_of_circle(5)  # ~78.54
result = mathio.perimeter_of_circle(5)  # ~31.42
result = mathio.area_of_triangle(10, 5)  # 25.0
result = mathio.area_of_rectangle(10, 5)  # 50.0
```
