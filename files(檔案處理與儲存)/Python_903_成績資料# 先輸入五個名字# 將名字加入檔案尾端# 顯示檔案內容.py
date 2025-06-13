# Python 903 成績資料

TQC+ 程式語言Python 903 成績資料
最新一次更新時間：2019-04-16 03:45:57

1. 題目說明:
請開啟PYD903.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA903.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端。之後再顯示此檔案的內容。

3. 輸入輸出：
輸入說明
輸入五個人的名字

輸出說明
讀取及寫入檔案後，輸出此檔案內容

範例輸入
Daisy
Kelvin
Tom
Joyce
Sarah
範例輸出
Append completed!
Content of "data.txt":
Ben
Cathy
Tony
Daisy
Kelvin
Tom
Joyce
Sarah
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

# PYA723.py

# 先輸入五個名字
names = [input() for _ in range(5)]

# 將名字加入檔案尾端
with open("data.txt", "a") as file:
    for name in names:
        file.write(name + "\n")

print("Append completed!")
print('Content of "data.txt":')

# 顯示檔案內容
with open("data.txt", "r") as file:
    content = file.read()
    print(content.strip())
