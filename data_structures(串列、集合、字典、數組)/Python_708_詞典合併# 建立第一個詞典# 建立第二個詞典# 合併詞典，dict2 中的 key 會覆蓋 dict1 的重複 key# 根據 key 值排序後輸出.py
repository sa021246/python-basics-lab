# Python 708 詞典合併

TQC+ 程式語言Python 708 詞典合併
最新一次更新時間：2023-05-12 10:18:08

1. 題目說明:
請開啟PYD708.py檔案，依下列題意進行作答，進行兩詞典合併，使輸出值符合題意要求。作答完成請另存新檔為PYA708.py再進行評分。

2. 設計說明：
請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。

3. 輸入輸出：
輸入說明
輸入兩個詞典，直至end結束輸入

輸出說明
合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create dict1:
Key: a
Value: apple
Key: b
Value: banana
Key: d
Value: durian
Key: end
Create dict2:
Key: c
Value: cat
Key: e
Value: elephant
Key: end
a: apple
b: banana
c: cat
d: durian
e: elephant

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格

Alt text

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

# PYA708.py

# 建立第一個詞典
print("Create dict1:")
dict1 = {}
while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    dict1[key] = value

# 建立第二個詞典
print("Create dict2:")
dict2 = {}
while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    dict2[key] = value

# 合併詞典，dict2 中的 key 會覆蓋 dict1 的重複 key
merged_dict = dict1.copy()
merged_dict.update(dict2)

# 根據 key 值排序後輸出
for key in sorted(merged_dict):
    print(f"{key}: {merged_dict[key]}")
