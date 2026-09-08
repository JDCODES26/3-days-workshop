def extract_digits(n, divisor):
    if divisor == 0:
        return
    digit = n // divisor
    print(digit)
    extract_digits(n % divisor, divisor // 10)

num = int(input("Enter a number: "))
divisor = 1
temp = num

while temp >= 10:
    divisor *= 10
    temp //= 10

extract_digits(num, divisor)
