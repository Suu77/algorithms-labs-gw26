def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))