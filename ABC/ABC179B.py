# O(n)

n = int(input())
zorome_count = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        zorome_count += 1
    else:
        zorome_count = 0

    if zorome_count == 3:
        print("Yes")
        break
if zorome_count != 3:
    print("No")

