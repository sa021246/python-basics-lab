# Python 506 一元二次方程式

TQC+ 程式語言Python 506 一元二次方程式
最新一次更新時間：2024-11-01 14:20:10

1. 題目說明:
請開啟PYD506.py檔案，依下列題意進行作答，依使用者輸入的數字作為參數傳遞進行公式計算，使輸出值符合題意要求。作答完成請另存新檔為PYA506.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式  的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

提示：
輸出有順序性，請先輸出包含正平方根的解，再輸出包含負平方根的解
回傳方程式的解，無須考慮小數點位數

3. 輸入輸出：
輸入說明
三個整數，分別為a、b、c

輸出說明
代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】

範例輸入1
2
-3
1
範例輸出1
1.0, 0.5
範例輸入2
9
9
8
範例輸出2
Your equation has no root.
範例輸入3
1
2
1
範例輸出3
-1.0
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#============================================================================

import math

def compute(a, b, c):
    delta = b ** 2 - 4 * a * c  # 計算判別式 Δ = b² - 4ac

    if delta < 0:
        print("Your equation has no root.")
    elif delta == 0:
        root = -b / (2 * a)
        print(root)
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"{root1}, {root2}")

# 讀取使用者輸入
try:
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())

    if a == 0:
        print("Your equation has no root.")  # 若 a = 0，則不是二次方程式
    else:
        compute(a, b, c)

except ValueError:
    print("Invalid input.")

