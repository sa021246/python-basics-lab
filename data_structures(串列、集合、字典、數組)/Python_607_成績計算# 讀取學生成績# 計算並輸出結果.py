# Python 607 成績計算

TQC+ 程式語言Python 607 成績計算
最新一次更新時間：2019-04-16 03:31:19

1. 題目說明:
請開啟PYD607.py檔案，依下列題意進行作答，顯示學生成績總分和平均分數，使輸出值符合題意要求。作答完成請另存新檔為PYA607.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。

提示：平均分數輸出到小數點後第二位。

3. 輸入輸出：
輸入說明
三位學生各五筆成績

輸出說明
格式化輸出每位學生的總分及平均分數

輸入與輸出會交雜如下，輸出的部份以粗體字表示
The 1st student:
78
89
88
70
60
The 2nd student:
90
78
66
68
78
The 3rd student:
69
97
70
89
90
Student 1
#Sum 385
#Average 77.00
Student 2
#Sum 380
#Average 76.00
Student 3
#Sum 415
#Average 83.00

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#===============================================================================

# 讀取學生成績
students = []
for i in range(3):
    print(f"The {i+1}st student:" if i == 0 else (f"The {i+1}nd student:" if i == 1 else f"The {i+1}rd student:"))
    scores = [int(input()) for _ in range(5)]
    students.append(scores)

# 計算並輸出結果
for i, scores in enumerate(students, 1):
    total = sum(scores)
    avg = total / len(scores)
    print(f"Student {i}")
    print(f"#Sum {total}")
    print(f"#Average {avg:.2f}")
