n = int(input("Enter a 3-digit number: "))

if 100 <= n <= 999:
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
else:
    print("Please enter a 3-digit number")