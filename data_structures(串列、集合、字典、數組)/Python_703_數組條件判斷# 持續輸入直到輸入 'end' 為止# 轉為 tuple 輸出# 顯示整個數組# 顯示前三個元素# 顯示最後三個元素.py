# Python 703 數組條件判斷

TQC+ 程式語言Python 703 數組條件判斷
最新一次更新時間：2019-04-16 03:34:42

1. 題目說明:
請開啟PYD703.py檔案，依下列題意進行作答，輸入字串至數組並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA703.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），以字串"end"為結束點（數組中不包含字串"end"）。接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

3. 輸入輸出：
輸入說明
至少輸入五個字串至數組，直至end結束輸入

輸出說明
數組
該數組的前三個元素
該數組最後三個元素

範例輸入
president
dean
chair
staff
teacher
student
end
範例輸出
('president', 'dean', 'chair', 'staff', 'teacher', 'student')
('president', 'dean', 'chair')
('staff', 'teacher', 'student')
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=================================================================================

# PYA703.py

data = []

# 持續輸入直到輸入 'end' 為止
while True:
    s = input()
    if s == "end":
        break
    data.append(s)

# 轉為 tuple 輸出
data_tuple = tuple(data)

# 顯示整個數組
print(data_tuple)

# 顯示前三個元素
print(data_tuple[:3])

# 顯示最後三個元素
print(data_tuple[-3:])
