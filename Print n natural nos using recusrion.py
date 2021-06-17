def print_from_start(n):
    if n == 1:
        print(n)
        return
    print_from_start(n - 1)
    print(n)



def print_from_end(n):
    if n == 1:
        print(n)
        return
    print(n)
    print_from_end(n-1)

x = int(input())
print_from_start(x)
print()
print()
print_from_end(x)
