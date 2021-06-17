def fact(n):
    if n == 1:
        return 1
    count = n * fact(n-1)
    return count

x = int(input())
print("Factorial is", fact(x))