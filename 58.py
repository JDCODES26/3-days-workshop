a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y:
    x, y = y, x % y

print("GCD of", a, "and", b, "is", x)
