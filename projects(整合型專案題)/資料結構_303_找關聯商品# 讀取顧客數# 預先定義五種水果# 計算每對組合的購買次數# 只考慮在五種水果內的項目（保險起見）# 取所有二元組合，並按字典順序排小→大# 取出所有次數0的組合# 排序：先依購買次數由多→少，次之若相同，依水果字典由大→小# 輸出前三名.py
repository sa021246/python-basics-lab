# 資料結構 303 找關聯商品

TQC+ 程式設計：資料結構 303 找關聯商品
最新一次更新時間：2024-05-08 13:11:08

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 水果行賣五種水果，分別為「apple」、「watermelon」、「pawpaw」、「banana」和「pineapple」，今天有 N（3 ≤ N ≤ 10）位顧客來買水果。

(2) 請撰寫一程式，讓使用者輸入 N 位顧客買的水果名稱，找出任兩種水果最常被顧客一起購買的前三名組合與購買次數。

提示：五種水果兩兩一組，共有十種組合。

3. 輸入輸出：
輸入說明
第 1 列：正整數 N（3 ≤ N ≤ 10），為顧客人數。
第 2~N+1 列：N 位顧客買水果的資料，資料間以一個半形空白間隔。

輸出說明
請依照購買次數「由多到少」，輸出前三名最常被顧客一起購買的水果組合（任兩種）與購買次數，中間以一個半形空白間隔。

註：
　- 水果組合，請依照水果名稱的字典「由小到大」排序。
　- 若購買次數相同，請依序按照水果名稱的字典「由大到小」排序。

範例輸入1
5
apple watermelon pawpaw
apple pawpaw banana
apple pawpaw pineapple
banana pineapple
watermelon banana pineapple
範例輸出1
apple pawpaw 3
banana pineapple 2
pineapple watermelon 1
範例輸入2
7
apple watermelon pawpaw banana
apple pawpaw banana
apple pawpaw pineapple
banana pineapple
watermelon banana pineapple
apple watermelon pineapple
apple watermelon
範例輸出2
apple watermelon 3
apple pawpaw 3
pineapple watermelon 2
待編修檔案

#=================================================================================

import itertools

# 讀取顧客數
N = int(input())

# 預先定義五種水果
fruits = ["apple", "watermelon", "pawpaw", "banana", "pineapple"]

# 計算每對組合的購買次數
from collections import Counter
pair_counts = Counter()

for _ in range(N):
    basket = input().split()
    # 只考慮在五種水果內的項目（保險起見）
    basket = [f for f in basket if f in fruits]
    # 取所有二元組合，並按字典順序排小→大
    for a, b in itertools.combinations(sorted(basket), 2):
        pair_counts[(a, b)] += 1

# 取出所有次數>0的組合
items = [(a, b, c) for (a, b), c in pair_counts.items()]

# 排序：先依購買次數由多→少，次之若相同，依水果字典由大→小
items.sort(key=lambda x: (-x[2], -ord(x[0][0]), -ord(x[1][0]), x[0], x[1]))

# 輸出前三名
for a, b, cnt in items[:3]:
    print(f"{a} {b} {cnt}")
