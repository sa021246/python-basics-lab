# Python 410 繪製等腰三角形

TQC+ 程式語言Python 410 繪製等腰三角形
最新一次更新時間：2019-04-16 03:19:39

1. 題目說明:
請開啟PYD410.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA410.py再進行評分。

2. 設計說明：
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
以 * 畫出等腰三角形
（每列最後一個 * 的右方無空白）

範例輸入
7
範例輸出
      *
     ***
    *****
   *******
  *********
 ***********
*************
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	20	0
總 分	20	0
待編修檔案

#================================================================================

n = int(input())

for i in range(n):
    spaces = n - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
