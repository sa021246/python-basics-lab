# 資料結構 102 二維陣列矩陣轉置運算

TQC+ 程式設計：資料結構 102 二維陣列矩陣轉置運算
最新一次更新時間：2024-05-07 17:07:55

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
請撰寫一程式，首先要求使用者輸入矩陣的列數（m）與行數（n），代表要創建矩陣  有 m x n 個元素，接著依序輸入 m x n 個元素值（皆為整數），請計算  的轉置矩陣 ，並輸出兩個矩陣  與 。

提示：矩陣（Matrix）指的是外觀為 m x n 的二維資料，其中  表示矩陣中第  列第  行的元素，而位置可表示成 。

提示：矩陣  的轉置（Transpose）是另一個矩陣 ，方法是將矩陣  中每個元素從位置  轉換到 。例如：
、

提示：輸出矩陣時，每列皆使用中括號（[、]）包覆，且整數間使用半形空白間隔。

3. 輸入輸出：
輸入說明
第 1 列：輸入矩陣的列數 m。
第 2 列：輸入矩陣的行數 n。
第 3~m*n+2 列：依序輸入矩陣元素（皆為整數）。

輸出說明
初始創建矩陣 
轉置後矩陣 
範例輸入1
2
3
1
2
3
4
5
6
範例輸出1
Original:
[1 2 3]
[4 5 6]
Transpose:
[1 4]
[2 5]
[3 6]
範例輸入2
3
3
-1
25
-5
33
100
-78
56
63
-99
範例輸出2
Original:
[-1 25 -5]
[33 100 -78]
[56 63 -99]
Transpose:
[-1 33 56]
[25 100 63]
[-5 -78 -99]
待編修檔案

#==================================================================================

# 輸入列數與行數
m = int(input())
n = int(input())

# 依序輸入 m * n 個整數，組成原始矩陣
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

# 計算轉置矩陣
transpose = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix[j][i])
    transpose.append(row)

# 輸出原始矩陣
print("Original:")
for row in matrix:
    print(f"[{' '.join(map(str, row))}]")

# 輸出轉置矩陣
print("Transpose:")
for row in transpose:
    print(f"[{' '.join(map(str, row))}]")
