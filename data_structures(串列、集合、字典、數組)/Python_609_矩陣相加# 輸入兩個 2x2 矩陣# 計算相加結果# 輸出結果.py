# Python 609 矩陣相加

TQC+ 程式語言Python 609 矩陣相加
最新一次更新時間：2023-05-12 10:16:14

1. 題目說明:
請開啟PYD609.py檔案，依下列題意進行作答，依輸入值建立2*2矩陣，並計算其相加結果，使輸出值符合題意要求。作答完成請另存新檔為PYA609.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。

3. 輸入輸出：
輸入說明
兩個2*2矩陣，皆輸入整數

輸出說明
矩陣1的內容
矩陣2的內容
矩陣1及矩陣2相加的結果

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter matrix 1:
[1, 1]: 3
[1, 2]: 5
[2, 1]: 7
[2, 2]: 5
Enter matrix 2:
[1, 1]: 6
[1, 2]: 9
[2, 1]: 8
[2, 2]: 3

Matrix 1:
3 5 
7 5 
Matrix 2:
6 9 
8 3 
Sum of 2 matrices:
9 14 
15 8 

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格

Alt text

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=================================================================================

def input_matrix(name):
    print(f"Enter {name}:")
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            value = int(input(f"[{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def print_matrix(name, matrix):
    print(f"{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

# 輸入兩個 2x2 矩陣
matrix1 = input_matrix("matrix 1")
matrix2 = input_matrix("matrix 2")

# 計算相加結果
sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

# 輸出結果
print_matrix("Matrix 1", matrix1)
print_matrix("Matrix 2", matrix2)
print_matrix("Sum of 2 matrices", sum_matrix)
