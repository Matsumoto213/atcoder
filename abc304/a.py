def print_names_in_order():
    N = int(input().strip())  # 人数Nを取得
    people = []
    for _ in range(N):
        name, age = input().strip().split()
        age = int(age)  # 年齢を整数に変換
        people.append((name, age))

    # 年齢が最小の人を見つけます
    min_age_index = 0
    for i in range(1, N):
        if people[i][1] < people[min_age_index][1]:
            min_age_index = i

    # 年齢が最も小さい人を起点にリストを回転させます
    people = people[min_age_index:] + people[:min_age_index]
    
    # その人の次から順に名前を出力します
    for i in range(N):
        print(people[i][0])

# 関数を実行
print_names_in_order()
