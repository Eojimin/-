horse = input()
row = ["1", "2", "3", "4", "5", "6", "7", "8"]
column = ["a", "b", "c", "d", "e", "f", "g", "h"]
count = 0
horse_position = []
horse_position.append(column.index(horse[0])+1)
horse_position.append(row.index(horse[1])+1)
dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]
for i in range(8):
    nx = horse_position[0] + dx[i]
    ny = horse_position[1] + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1
print(count)