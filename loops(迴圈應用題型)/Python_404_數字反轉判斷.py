# Python 404 數字反轉判斷

TQC+ 程式語言Python 404 數字反轉判斷
最新一次更新時間：2019-04-16 03:16:28

1. 題目說明:
請開啟PYD404.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA404.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0。

3. 輸入輸出：
輸入說明
一個正整數或0

輸出說明
正整數反轉輸出。如輸入數值為0，輸出為0

範例輸入1
31283
範例輸出1
38213
範例輸入2
0
範例輸出2
0
範例輸入3
135790
範例輸出3
097531
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	20	0
總 分	20	0
待編修檔案

#===============================================================================

n = input()

if n == '0':
    print('0')
else:
    print(n[::-1])