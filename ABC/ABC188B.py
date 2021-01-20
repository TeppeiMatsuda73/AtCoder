n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_sum = 0
for i in range(n):
    list_sum += list_a[i] * list_b[i]

print("Yes" if list_sum == 0 else "No")
