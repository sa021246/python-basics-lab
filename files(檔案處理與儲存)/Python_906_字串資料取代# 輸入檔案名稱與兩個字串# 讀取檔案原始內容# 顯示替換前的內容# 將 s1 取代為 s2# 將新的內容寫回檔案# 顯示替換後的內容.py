# Python 906 字串資料取代

TQC+ 程式語言Python 906 字串資料取代
最新一次更新時間：2019-04-16 03:47:42

1. 題目說明:
請開啟PYD906.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA906.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。

3. 輸入輸出：
輸入說明
輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）

輸出說明
輸出檔案中的內容
輸出取代指定字串後的檔案內容

範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#====================================================================================

# PYA726.py

# 輸入檔案名稱與兩個字串
filename = input()
s1 = input()
s2 = input()

# 讀取檔案原始內容
with open(filename, "r") as file:
    lines = file.readlines()

# 顯示替換前的內容
print("=== Before the replacement")
for line in lines:
    print(line.strip())

# 將 s1 取代為 s2
replaced_lines = [line.replace(s1, s2) for line in lines]

# 將新的內容寫回檔案
with open(filename, "w") as file:
    file.writelines(replaced_lines)

# 顯示替換後的內容
print("=== After the replacement")
for line in replaced_lines:
    print(line.strip())

