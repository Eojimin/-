N = int(input())
X = list(input().split())
user = [1, 1]
row = user[0]
column = user[1]
for i in X:
    if i == "R" and column < N:
        column += 1
    elif i == "L" and column > 1:
        column -= 1
    elif i == "U" and row > 1:
        row -= 1
    elif i == "D" and row < N:
        row += 1
user[0] = row
user[1] = column
print(user)

