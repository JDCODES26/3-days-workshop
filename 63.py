x = float(input("Enter base: "))
n = int(input("Enter exponent: "))

result = 1
for _ in range(abs(n)):
    result *= x

if n < 0:
    result = 1 / result

print(f"{x}^{n} = {result}")
