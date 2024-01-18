def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: multiply n with factorial of (n-1)
    return n * factorial(n - 1)
