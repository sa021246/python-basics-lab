# Python 605 成績計算

TQC+ 程式語言Python 605 成績計算
最新一次更新時間：2019-04-16 03:30:18

1. 題目說明:
請開啟PYD605.py檔案，依下列題意進行作答，去除最高最低分後加總其餘成績，使輸出值符合題意要求。作答完成請另存新檔為PYA605.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。

提示：平均值輸出到小數點後第二位。

3. 輸入輸出：
輸入說明
十個數字

輸出說明
總和
平均

範例輸入
89
78
67
80
75
98
77
89
76
60
範例輸出
631
78.88
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案
#================================================================================

# 讀取 10 個成績
scores = [int(input()) for _ in range(10)]

# 去除最大值與最小值
scores.remove(max(scores))
scores.remove(min(scores))

# 計算總和與平均值
total = sum(scores)
average = total / len(scores)

# 輸出結果
print(total)
print(f"{average:.2f}")
