def sum(n):
    if n == 1:
        return 1
    summation = n + sum(n-1)
    return summation

x = int(input())
print("Sum of n natural nos is", sum(x))
