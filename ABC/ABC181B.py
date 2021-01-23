n = int(input())
num_list = [list(map(int, input().split())) for n in range(n)]

sum_all = 0
for i in num_list:
    if (i[1]-i[0])%2 == 0 :
        # こんなのいらない。なんか意味不明なことしてた
        sum_all += (((i[1]-1) + i[0]) * (i[1]-i[0]) / 2) + i[1]
    else:
        sum_all += (i[1] + i[0]) * (i[1]-i[0] + 1) / 2

print(int(sum_all))

