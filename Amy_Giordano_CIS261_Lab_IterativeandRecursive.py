#Amy Giordano
#CIS261
#Iterative and Recursive Functionality Lab Week 8




# Iterative function to calculate the factorial
def fact_iterative(n):
    f = 1 
    for i in range(1, n+1):
        f = f * i 
    return f 

# Recursive function to calculate the factorial
def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

# Call each function from a print statement five times
print(fact_recursive(0))
print(fact_iterative(0))
print(fact_recursive(5))
print(fact_iterative(5))
print(fact_recursive(10))
print(fact_iterative(10))
print(fact_recursive(25))
print(fact_iterative(25))
print(fact_recursive(50))
print(fact_iterative(50))