n, x = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]
x *= 100  # 本当は%で示すために/100をするのだが、浮動小数点の罠を回避するためにこのようにする
total_ml = 0
ans = -1
count = 0
for i in v:
    total_ml += i[0] * i[1]
    count += 1
    if total_ml > x:
        ans = count
        break

print(ans)

