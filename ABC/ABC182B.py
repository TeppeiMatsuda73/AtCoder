n = int(input())
a = list(map(int, input().split()))
max_gcd = 0
max_gcd_num = 0
for i in range(2, max(a)+1):
    gcd_qua = 0
    for j in a:
        if j%i==0:
            gcd_qua += 1

    if gcd_qua > max_gcd:
        max_gcd = gcd_qua
        max_gcd_num = i

print(max_gcd_num)

