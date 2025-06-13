# Python 909 聯絡人資料

TQC+ 程式語言Python 909 聯絡人資料
最新一次更新時間：2019-04-16 03:49:16

1. 題目說明:
請開啟PYD909.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA909.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.dat檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，將使用者輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。再將檔案加以讀取並顯示檔案內容。

3. 輸入輸出：
輸入說明
五個人的姓名和電話號碼，以空白分隔

輸出說明
讀取及寫入檔案後，再輸出讀入的檔案名稱及內容

範例輸入
Karen 123456789
Bonnie 235689147
Simon 987612345
Louis 675489321
Andy 019238475
範例輸出
The content of "data.dat":
Karen 123456789

Bonnie 235689147

Simon 987612345

Louis 675489321

Andy 019238475

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

# PYA729.py

# 檔案名稱
filename = "data.dat"

# 接收並寫入五筆資料
with open(filename, "w") as file:
    for _ in range(5):
        data = input()
        file.write(data + "\n")

# 讀取並顯示檔案內容
print(f'The content of "{filename}":')
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
        print()
