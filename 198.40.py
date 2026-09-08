balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = float(input("Enter minimum balance required: "))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: minimum balance rule violated")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)