rows = 6
cols = 7

pattern = [
    [0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for i in range(rows):
    row = ""
    for j in range(cols):
        row += "*" if pattern[i][j] == 1 else " "
    print(row)
