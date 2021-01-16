def sum_num(a):
    x = 0
    for i in range(0, len(a)):
        x += int(a[i])
    return x

a, b = map(str, input().split())
A = sum_num(a)
B = sum_num(b)

print( A if A >= B else B)
