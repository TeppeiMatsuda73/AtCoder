sx, sy, gx, gy = map(int, input().split())
# sy : gy = sx :
xx = abs(sx - gx)
tx = xx / (sy + gy) * sy
if sx < gx:
    print(sx + tx)
else:
    print(sx - tx)
