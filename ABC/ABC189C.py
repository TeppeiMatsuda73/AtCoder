# TLEで通らない O(n^2)
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(len(a)):
#     for j in range(i, len(a)):
#         a_min = min(a[i:j+1])
#         total = a_min * (j - i + 1)
#         if total > ans:
#             ans = total
# print(ans)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(len(a)):
    for j in range(i, len(a)):
        a_min = min(a[i:j+1])
        total = a_min * (j - i + 1)
        if total > ans:
            ans = total
print(ans)

