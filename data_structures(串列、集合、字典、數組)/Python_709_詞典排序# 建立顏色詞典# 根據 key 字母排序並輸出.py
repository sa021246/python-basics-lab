# Python 709 詞典排序

TQC+ 程式語言Python 709 詞典排序
最新一次更新時間：2019-04-16 03:38:48

1. 題目說明:
請開啟PYD709.py檔案，依下列題意進行作答，輸入顏色詞典並進行排序，使輸出值符合題意要求。作答完成請另存新檔為PYA709.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入一顏色詞典color_dict（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再根據key值的字母由小到大排序並輸出。

3. 輸入輸出：
輸入說明
輸入一個詞典，直至end結束輸入

輸出說明
根據key值字母由小到大排序輸出

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Key: Green Yellow
Value: #ADFF2F
Key: Snow
Value: #FFFAFA
Key: Gold
Value: #FFD700
Key: Red
Value: #FF0000
Key: White
Value: #FFFFFF
Key: Green
Value: #008000
Key: Black
Value: #000000
Key: end
Black: #000000
Gold: #FFD700
Green: #008000
Green Yellow: #ADFF2F
Red: #FF0000
Snow: #FFFAFA
White: #FFFFFF

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=================================================================================

# PYA709.py

# 建立顏色詞典
color_dict = {}

while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    color_dict[key] = value

# 根據 key 字母排序並輸出
for key in sorted(color_dict):
    print(f"{key}: {color_dict[key]}")
