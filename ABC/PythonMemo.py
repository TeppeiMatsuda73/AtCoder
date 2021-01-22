
list = (1, 2, 3, 4, 5, 6)

# 最小値を求める
min(list)  # --> 1

# 最大値を求める
max(list)  # --> 6

# リストのサイズを求める
len(list)  # --> 6
# 文字列のサイズを求める
len("あいうえお")  # --> 5

# リストをn次元で格納(線形代数ってやつ？)
# extend_list = [list(map(int, input().split())) for i in range(n)]

# リストへの要素追加
ex_list = [1, 3]
# リストそのものが追加される
ex_list.append([5, 7, 9])  # --> [1, 3, [5, 7, 9]]
# リスト内の要素が追加される
ex_list.extend([4, 6, 8])  # --> [1, 3, [5, 7, 9], 4, 6, 8]

# forループで複数のリストの要素を取得
# zip:多い分の要素が虫される
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18, 30]
for name, age in zip(names, ages):
    print(name, age)  # --> Alice 24  Bob 50  Charlie 18
# zip_longest:足りない分の要素が埋められる
# fillvalueを指定で、足りない分をデフォルトで埋める
# for name, age in zip_longest(name, age, fillvalue="Dave")
#     print(name, age)  # --> Alice 24  Bob 50  Charlie 18  Dave 30


