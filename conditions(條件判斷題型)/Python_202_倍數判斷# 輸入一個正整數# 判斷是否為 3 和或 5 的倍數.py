# Python 202 倍數判斷

TQC+ 程式語言Python 202 倍數判斷
最新一次更新時間：2021-07-19 16:22:51

1. 題目說明:
請開啟PYD202.py檔案，依下列題意進行作答，判斷輸入值是否為3或5的倍數，使輸出值符合題意要求。作答完成請另存新檔為PYA202.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】或【x is a multiple of 5.】；若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為3或者是5的倍數

範例輸入1
55
範例輸出1
55 is a multiple of 5.
範例輸入2
36
範例輸出2
36 is a multiple of 3.
範例輸入3
92
範例輸出3
92 is not a multiple of 3 or 5.
範例輸入4
15
範例輸出4
15 is a multiple of 3 and 5.
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=======================================================

# 輸入一個正整數
num = int(input())

# 判斷是否為 3 和/或 5 的倍數
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is a multiple of 3 and 5.")
elif num % 3 == 0:
    print(f"{num} is a multiple of 3.")
elif num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 3 or 5.")

