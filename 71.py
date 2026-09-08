num = int(input("Enter a decimal number: "))

if num == 0:
    binary = "0"
else:
    binary = ""
    temp = num
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2

print("Binary:", binary)
