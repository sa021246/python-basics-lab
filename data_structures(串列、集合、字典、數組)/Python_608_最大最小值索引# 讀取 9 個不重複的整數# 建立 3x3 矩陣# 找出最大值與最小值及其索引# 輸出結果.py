# Python 608 最大最小值索引

TQC+ 程式語言Python 608 最大最小值索引
最新一次更新時間：2019-04-16 03:31:45

1. 題目說明:
請開啟PYD608.py檔案，依下列題意進行作答，建立3*3矩陣並輸出矩陣最大值與最小值的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA608.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#===============================================================================

# 讀取 9 個不重複的整數
nums = [int(input()) for _ in range(9)]

# 建立 3x3 矩陣
matrix = [nums[i:i+3] for i in range(0, 9, 3)]

# 找出最大值與最小值及其索引
max_val = max(nums)
min_val = min(nums)
max_idx = [(i, j) for i in range(3) for j in range(3) if matrix[i][j] == max_val][0]
min_idx = [(i, j) for i in range(3) for j in range(3) if matrix[i][j] == min_val][0]

# 輸出結果
print(f"Index of the largest number {max_val} is: {max_idx}")
print(f"Index of the smallest number {min_val} is: {min_idx}")
