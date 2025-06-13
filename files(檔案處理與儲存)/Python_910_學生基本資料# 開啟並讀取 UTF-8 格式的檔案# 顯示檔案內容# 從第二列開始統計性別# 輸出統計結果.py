# Python 910 學生基本資料

TQC+ 程式語言Python 910 學生基本資料
最新一次更新時間：2019-04-16 03:49:50

1. 題目說明:
請開啟PYD910.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA910.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.dat檔案為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。

3. 輸入輸出：
輸入說明
讀取read.dat

輸出說明
讀取檔案內容，並格式化輸出男生人數和女生人數

範例輸入
無

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

# PYA730.py

# 開啟並讀取 UTF-8 格式的檔案
filename = "read.dat"
male_count = 0
female_count = 0

with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 顯示檔案內容
for line in lines:
    print(line.strip())

# 從第二列開始統計性別
for line in lines[1:]:
    parts = line.strip().split()
    if len(parts) >= 3:
        gender = parts[2]
        if gender == '0':
            female_count += 1
        elif gender == '1':
            male_count += 1

# 輸出統計結果
print(f"Number of males: {male_count}")
print(f"Number of females: {female_count}")


