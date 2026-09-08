n=int(input("enter a number:"))

if n%3==0 & n%5==0:
    print("the number is divisible by 3 and 5")
elif n%3==0:
    print("the number is divisible by 3")
elif n%5==0:
    print("the number is divisible by 5")
else:
    print("number is neither divisble by 3 and 5")
