n = int(input())
a = list(map(int, input().split()))
a_sub = list(set(a))
sorted(a_sub, reverse=True)
for i in range(len(a_sub)):
    for j in range(i+1, len(a_sub)-1):
        if a_sub[i] >= a_sub[j]*n:
            a_sub.remove(a_sub[j])

max_orange = 0
for i in a_sub:
    total = 0
    for j in a:
        if i <= j:
            total += i

        if total != 0 and i > j:
            if max_orange < total:
                max_orange = total
                total = 0
        if max_orange < total:
            max_orange = total


print(max_orange)