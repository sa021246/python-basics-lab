# Python 907 詳細資料顯示

TQC+ 程式語言Python 907 詳細資料顯示
最新一次更新時間：2019-04-16 03:48:13

1. 題目說明:
請開啟PYD907.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA907.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名read.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。

3. 輸入輸出：
輸入說明
讀取read.txt

輸出說明
行數
單字數
字元數（不含空白）

範例輸入
read.txt
範例輸出
6 line(s)
102 word(s)
614 character(s)
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=================================================================================

# PYA727.py

# 輸入檔案名稱
filename = input()

# 開啟檔案並讀取內容
with open(filename, 'r') as file:
    lines = file.readlines()

# 計算行數
line_count = len(lines)

# 計算單字數（以空白分隔）
word_count = sum(len(line.split()) for line in lines)

# 計算字元數（不含空白）
char_count = sum(len(line.replace(" ", "").replace("\n", "")) for line in lines)

# 輸出結果
print(f"{line_count} line(s)")
print(f"{word_count} word(s)")
print(f"{char_count} character(s)")

