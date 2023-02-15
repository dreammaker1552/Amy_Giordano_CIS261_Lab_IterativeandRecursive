#Amy Giordano
#CIS261
#Iterative and Recursive Functionality Lab Week 9




# Factorial results using an iterative function
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Factorial results using a recursive function
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Call each function from a print statement with different input values
for i in range(1, 6):
    print(f"Factorial of {i} (iterative): {factorial_iterative(i)}")
    print(f"Factorial of {i} (recursive): {factorial_recursive(i)}")

