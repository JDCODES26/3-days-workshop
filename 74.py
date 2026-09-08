x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

result = 0
sign = 1

for i in range(1, n + 1):
    power = 2 * i - 1
    factorial = 1
    for j in range(1, power + 1):
        factorial *= j
    result += sign * (x ** power) / factorial
    sign *= -1

print("sin(x) approx:", result)
