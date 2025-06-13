# Python 610 平均溫度

TQC+ 程式語言Python 610 平均溫度
最新一次更新時間：2023-05-12 10:17:14

1. 題目說明:
請開啟PYD610.py檔案，依下列題意進行作答，依輸入值計算四週的平均溫度及最高、最低溫度，使輸出值符合題意要求。作答完成請另存新檔為PYA610.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

3. 輸入輸出：
輸入說明
四週各三天的溫度

輸出說明
平均溫度
最高溫度
最低溫度

輸入與輸出會交雜如下，輸出的部份以粗體字表示
下圖中的 粉紅色點 為 空格

Week 1:
Day 1:23.1
Day 2:24
Day 3:23.5
Week 2:
Day 1:32
Day 2:33
Day 3:35.3
Week 3:
Day 1:29
Day 2:30
Day 3:26
Week 4:
Day 1:27.6
Day 2:25
Day 3:28.8
Average: 28.11
Highest: 35.3
Lowest: 23.1

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#==============================================================

# 初始化存放溫度的列表
temperatures = []

# 讀取使用者輸入的四週溫度，每週三天
for week in range(4):
    temps = list(map(float, input().split()))
    temperatures.extend(temps)

# 計算平均溫度，保留兩位小數
average_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

# 輸出結果
print(f"{average_temp:.2f}")
print(max_temp)
print(min_temp)
