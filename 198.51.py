n = int(input("Enter a number: "))

original = n
reverse = 0
temp = abs(n)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")