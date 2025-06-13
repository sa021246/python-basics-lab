# Python 905 字串資料刪除

TQC+ 程式語言Python 905 字串資料刪除
最新一次更新時間：2019-04-16 03:47:13

1. 題目說明:
請開啟PYD905.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA905.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。

3. 輸入輸出：
輸入說明
輸入data.txt及一個字串

輸出說明
先輸出原檔案內容，再輸入刪除指定字串後的新檔案內容

範例輸入1
data.txt
Tomato
範例輸出1
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian

=== After the deletion
Apple Kiwi Banana
 Pear Durian
 
範例輸入2
data.txt
Kiwi
範例輸出2
=== Before the deletion
Apple Kiwi Banana
Tomato Pear Durian

=== After the deletion
Apple  Banana
Tomato Pear Durian

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#===============================================================================

# PYA725.py

# 輸入檔案名稱與要刪除的字串
filename = input()
target = input()

# 讀取原始內容
with open(filename, "r") as file:
    lines = file.readlines()

# 顯示刪除前內容
print("=== Before the deletion")
for line in lines:
    print(line.strip())

# 刪除指定字串
updated_lines = [line.replace(target, "") for line in lines]

# 將新內容寫回檔案
with open(filename, "w") as file:
    file.writelines(updated_lines)

# 顯示刪除後內容
print("\n=== After the deletion")
for line in updated_lines:
    print(line.strip())

