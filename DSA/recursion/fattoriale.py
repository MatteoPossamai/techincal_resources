def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# DOES  NOT MAKE SENSE TO HAVE A RECORD, BECAUSE THERE IS ONLY ONE
# CALL THROUGH THE STACK OF RECURSION, SO THIS MAKES NOT THE 
# COMPUTATION TIME LOWER, BUT CAN ALSO MAKE IT SLOWER BECAUSE 
# NOW IT HAS ALSO TO COPY INTO A STRUCTURE, ERGO WORSE SPACE
# COMPLEXITY
def factorial_with_memory(n, calculated={}):
    if n==0:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = n * factorial_with_memory(n-1)
        return calculated[n]

## MAIN
a = 200
print(factorial(a))
print(factorial_with_memory(a))