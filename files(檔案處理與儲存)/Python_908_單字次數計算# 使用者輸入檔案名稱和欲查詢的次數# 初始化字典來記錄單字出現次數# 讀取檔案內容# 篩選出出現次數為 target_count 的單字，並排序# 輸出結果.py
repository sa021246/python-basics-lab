# Python 908 單字次數計算

TQC+ 程式語言Python 908 單字次數計算
最新一次更新時間：2019-04-16 03:48:49

1. 題目說明:
請開啟PYD908.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA908.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

3. 輸入輸出：
輸入說明
讀取read.txt的內容，以及檔案中某單字出現的次數

輸出說明
輸出符合次數的單字，並依單字的第一個字母大小排序

範例輸入
read.txt
3
範例輸出
a
is
programming
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#===================================================================================

# PYA728.py

# 使用者輸入檔案名稱和欲查詢的次數
filename = input()
target_count = int(input())

# 初始化字典來記錄單字出現次數
word_count = {}

# 讀取檔案內容
with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# 篩選出出現次數為 target_count 的單字，並排序
matched_words = sorted([word for word, count in word_count.items() if count == target_count])

# 輸出結果
for word in matched_words:
    print(word)

