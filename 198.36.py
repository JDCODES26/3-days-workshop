cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))

if selling > cost:
    print("Profit =", selling - cost)
elif selling < cost:
    print("Loss =", cost - selling)
else:
    print("No profit, no loss")