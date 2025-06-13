# Python 702 數組合併排序

TQC+ 程式語言Python 702 數組合併排序
最新一次更新時間：2019-04-16 03:34:06

1. 題目說明:
請開啟PYD702.py檔案，依下列題意進行作答，將兩數組合併並進行排序，使輸出值符合題意要求。作答完成請另存新檔為PYA702.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

3. 輸入輸出：
輸入說明
兩個數組，直至-9999結束輸入

輸出說明
排序前的數組
排序後的串列

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

print("Create tuple1:")
list1 = []
while True:
    n = int(input())
    if n == -9999:
        break
    list1.append(n)
tuple1 = tuple(list1)

print("Create tuple2:")
list2 = []
while True:
    n = int(input())
    if n == -9999:
        break
    list2.append(n)
tuple2 = tuple(list2)

# 合併並輸出排序前的元組
combined_tuple = tuple1 + tuple2
print("Combined tuple before sorting:", combined_tuple)

# 轉為串列後排序
sorted_list = sorted(combined_tuple)
print("Combined list after sorting:", sorted_list)

