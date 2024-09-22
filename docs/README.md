# Mathio

A comprehensive Python library for various mathematical operations, including basic arithmetic, trigonometry, algebra, calculus, statistics, and geometry.

## Features
- Basic arithmetic (addition, subtraction, multiplication, division)
- Trigonometric functions (sin, cos, tan)
- Roots (square root, cube root)
- Logarithms (natural log)
- Algebra (solving linear equations, quadratic formula)
- Calculus (derivatives, definite integrals)
- Statistics (mean, median, mode, standard deviation)
- Geometry (areas and perimeters of common shapes)

## Installation

To install the library, clone the repository and import the modules in your project.

## Usage

Here are examples for how to use various functions from the library:

```python
import mathio

# Basic operations
result = mathio.add(5, 3)  # 8

# Trigonometry
result = mathio.sin(1.5708)  # ~1.0

# Roots
result = mathio.square_root(16)  # 4.0

# Calculus
def func(x):
    return x**2
deriv = mathio.derivative(func, 3)  # 6.0
integral = mathio.definite_integral(func, 0, 2)  # 2.66667
```

For detailed usage, see the [documentation](docs/usage.md).
