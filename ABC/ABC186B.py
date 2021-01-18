H, W = map(int, input().split())
a = [list(map(int, input().split())) for n in range(H)]
min_value = 100
for i in range(H):
    for j in range(W):
        if min_value >= a[i][j]:
            min_value = a[i][j]

delete_block = 0
for i in range(H):
    for j in range(W):
        if min_value < a[i][j]:
            delete_block += (a[i][j] - min_value)

print(delete_block)
