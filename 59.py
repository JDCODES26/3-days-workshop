a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y:
    x, y = y, x % y
gcd = x

lcm = (a * b) // gcd
print("LCM of", a, "and", b, "is", lcm)
