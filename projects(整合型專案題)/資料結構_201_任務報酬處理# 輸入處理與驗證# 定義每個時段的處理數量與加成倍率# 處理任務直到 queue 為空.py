# 資料結構 201 任務報酬處理

TQC+ 程式設計：資料結構 201 任務報酬處理
最新一次更新時間：2024-05-08 09:38:06

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 冒險者每天能處理任務的時間有限，一天之中分成「早、中、晚」三個時段可以處理，每個時段可處理的任務數量及報酬金加成資訊如下：

早：最多可處理 3 個任務，且報酬金 x 3。
中：最多可處理 2 個任務，且報酬金 x 2。
晚：只能處理 1 個任務，報酬金無加成。
(2) 若任務數量超過一天能處理的量，則會順延到隔天，直到所有任務處理完為止。

(3) 請讓使用者輸入一個正整數佇列，代表公會給他的任務清單，先收到的任務先處理。
例如：「100,200,500」，每個數字代表任每項務報酬金，數字之間用半形逗號（,）隔開，若輸入 n 個數字代表總共有 n 個任務。

(4) 請使用佇列（Queue）的方式，為冒險者排程並完成所有任務，最後輸出他完成所有任務後，賺取的總報酬金。

3. 輸入輸出：
輸入說明
一個以半形逗號間隔的正整數佇列，代表任務清單。

輸出說明
完成所有任務後，得到的總報酬金。

若輸入的佇列中包含非正整數的值，則直接輸出「error」。

範例輸入1
100,200,500
範例輸出1
2400
範例輸入2
500,400,300,200,100
範例輸出2
4200
待編修檔案

#===================================================================================

from collections import deque

# 輸入處理與驗證
try:
    raw_input = input()
    tasks = raw_input.split(",")
    queue = deque()
    for task in tasks:
        task = task.strip()
        if not task.isdigit() or int(task) <= 0:
            raise ValueError
        queue.append(int(task))
except:
    print("error")
    exit()

# 定義每個時段的處理數量與加成倍率
time_slots = [
    (3, 3),  # 早上：最多處理3件，加成x3
    (2, 2),  # 中午：最多處理2件，加成x2
    (1, 1)   # 晚上：最多處理1件，加成x1
]

total_reward = 0

# 處理任務直到 queue 為空
while queue:
    for limit, multiplier in time_slots:
        for _ in range(limit):
            if queue:
                task_reward = queue.popleft()
                total_reward += task_reward * multiplier
            else:
                break

print(total_reward)
