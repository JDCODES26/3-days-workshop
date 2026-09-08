age = int(input("Enter age: "))

if age < 13:
    price = 50
elif age < 60:
    price = 100
else:
    price = 70

print("Ticket price = ₹", price)