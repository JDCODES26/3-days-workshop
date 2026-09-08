num = int(input("Enter a number: "))

temp = abs(num)
largest = -1
smallest = 10

while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    temp //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)
