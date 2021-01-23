n = int(input())
xy_list = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(len(xy_list)):
    if i == len(xy_list) - 1:
        break
    for j in range(i+1, len(xy_list)):
        katamuki = (xy_list[i][1] - xy_list[j][1]) / (xy_list[i][0] - xy_list[j][0])
        if -1 <= katamuki <= 1:
            ans += 1

print(ans)
