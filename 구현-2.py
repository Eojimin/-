N = int(input())
count = 0

for h in range(N+1):
    if "3" in str(h):
        count += 60 * 60
    else:
        for m in range(60):
            if "3" in str(m):
                count += 60
            else:
                count += 15
print(count)