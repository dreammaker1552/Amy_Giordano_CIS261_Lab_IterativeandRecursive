#Amy Giordano
#CIS261
#Iterative and Recursive Functionality Lab Week 8




# Factorial results using an iterative function
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
# Factorial results using a recursive function
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    for num in [0, 5, 10, 25, 50, 100]:
        print("Factorial of", num, "using iterative function:", factorial_iterative(num))
        print("Factorial of", num, "using recursive function:", factorial_recursive(num))



