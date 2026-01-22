def sum(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b 
def average(a, b):
    return (a + b) / 2
def max_value(a, b):
    return max(a, b)
def min_value(a, b):
    return min(a, b)
def absolute(a):
    return abs(a)
def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return a ** 0.5
def cube_root(a):
    return a ** (1/3)
def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
def logarithm(a, base=10):
    import math
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)
def natural_log(a):
    import math
    if a <= 0:
        raise ValueError("Natural logarithm undefined for non-positive values.")
    return math.log(a)
def exponential(a):
    import math
    return math.exp(a)
def sine(a):
    import math
    return math.sin(a)
def cosine(a):
    import math
    return math.cos(a)
def tangent(a): 
    import math
    return math.tan(a)
def arcsine(a):
    import math
    if a < -1 or a > 1:
        raise ValueError("Arcsine undefined for values outside the range [-1, 1].")
    return math.asin(a)
def arccosine(a):
    import math
    if a < -1 or a > 1:
        raise ValueError("Arccosine undefined for values outside the range [-1, 1].")
    return math.acos(a)
def arctangent(a):
    import math
    return math.atan(a)
def hyperbolic_sine(a):
    import math
    return math.sinh(a)
def hyperbolic_cosine(a):
    import math
    return math.cosh(a)
def hyperbolic_tangent(a):
    import math
    return math.tanh(a)
def degrees_to_radians(deg):
    import math
    return deg * (math.pi / 180)
def radians_to_degrees(rad):
    import math
    return rad * (180 / math.pi)
def round_value(a, digits=0):
    return round(a, digits)
def ceiling(a): 
    import math
    return math.ceil(a)
def floor(a):
    import math
    return math.floor(a)