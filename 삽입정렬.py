array = [3, 7, 6, 2, 1, 8, 9, 0, 4, 5]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)