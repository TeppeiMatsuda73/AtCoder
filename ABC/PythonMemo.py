
list = (1, 2, 3, 4, 5, 6)

# 最小値を求める
min(list)  # --> 1

# 最大値を求める
max(list)  # --> 6

# 配列のサイズを求める
len(list)  # --> 6

# リストをn次元で格納(線形代数ってやつ？)
# extend_list = [list(map(int, input().split())) for i in range(n)]

# リストへの要素追加
ex_list = [1, 3]
# リストそのものが追加される
ex_list.append([5, 7, 9])  # --> [1, 3, [5, 7, 9]]
# リスト内の要素が追加される
ex_list.extend([4, 6, 8])  # --> [1, 3, [5, 7, 9], 4, 6, 8]
