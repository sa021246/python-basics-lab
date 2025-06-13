# 資料結構 101 總分計算

TQC+ 程式設計：資料結構 101 總分計算
最新一次更新時間：2024-05-03 13:49:01

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
請協助國小的班導師，設計一個程式，讓導師依次輸入學生的姓名、國文、英文和數學成績後，計算每位學生的成績總分與平均，並根據成績總分「由高至低」輸出結果。

3. 輸入輸出：
輸入說明
每一列依序輸入學生的姓名、國文、英文和數學成績，所有資料皆以半形空白間隔，直到該列輸入「END」表示結束。

註：姓名格式為英文字串（長度不超過20個字元）；成績格式為 0 或正整數。

輸出說明
根據成績總分「由高至低」，依序輸出學生的姓名、國文成績、英文成績、數學成績、成績總分與平均（平均值請四捨五入至小數點後第二位），所有資料皆以半形空白間隔。

若成績總分相同，則依照資料輸入的先後順序輸出，即先輸入者先輸出。

範例輸入1
James 80 90 70
John 60 75 80
Carol 90 80 65
END
範例輸出1
James 80 90 70 240 80.00
Carol 90 80 65 235 78.33
John 60 75 80 215 71.67
範例輸入2
Robert 74 90 70
Michael 60 75 80
Linda 90 80 65
Barbara 75 85 60
William 45 90 90
END
範例輸出2
Linda 90 80 65 235 78.33
Robert 74 90 70 234 78.00
William 45 90 90 225 75.00
Barbara 75 85 60 220 73.33
Michael 60 75 80 215 71.67
待編修檔案

#================================================================================

students = []
order = 0  # 保留輸入順序以便排序時使用

while True:
    line = input()
    if line == "END":
        break
    data = line.split()
    name = data[0]
    chinese = int(data[1])
    english = int(data[2])
    math = int(data[3])
    total = chinese + english + math
    average = round(total / 3, 2)
    students.append((total, order, name, chinese, english, math, average))
    order += 1

# 依照總分排序，總分高者優先，若相同則依輸入順序
students.sort(key=lambda x: (-x[0], x[1]))

for student in students:
    print(f"{student[2]} {student[3]} {student[4]} {student[5]} {student[0]} {student[6]:.2f}")
