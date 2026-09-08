n = int(input("Enter number of rows: "))

for i in range(n):
    ch = chr(65 + i)
    print((ch + " ") * (i + 1))
