def recursive_fibonacci_1(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci_1(n-1) + recursive_fibonacci_1(n-2)

# MAKES SENSE TO KEEP TRACK OF THE ALREADY CALCULATED NUMBERS BECAUSE OTHERWISE
# YOU WILL NEED TO COMPUTE THEM TWICE, BECAUSE YOU CALL IT RECURSIVELY TWICE.
# ONCE YOU HAVE DONE WITH THE FIRST TRY, YOU ARE DONE ALSO WITH THE SECOND IN 
# O(n) TIME, BECAUSE IT ONLY NEEDS TO GET FROM AN HASHMAP A VALUE
def recursive_fibonacci_2(n: int, calculated={}) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = recursive_fibonacci_2(n-1, calculated) + recursive_fibonacci_2(n-2, calculated)
        return calculated[n]

## MAIN
print("Fibonacci Sequence")
print("Recursive Fibonacci 1")
print(recursive_fibonacci_1(33))
print("Recursive Fibonacci 2")
print(recursive_fibonacci_2(100))