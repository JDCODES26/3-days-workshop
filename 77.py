def print_numbers(i, n):
    if i > n:
        return
    print(i)
    print_numbers(i + 1, n)
    print(i)

n = int(input("Enter N: "))
print_numbers(1, n)
