# Python 309 存款總額

TQC+ 程式語言Python 309 存款總額
最新一次更新時間：2019-04-16 03:12:50

1. 題目說明:
請開啟PYD309.py檔案，依下列題意進行作答，計算每個月的存款總額，使輸出值符合題意要求。作答完成請另存新檔為PYA309.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，提示使用者輸入金額（如10,000）、年收益率（如5.75），以及經過的月份數（如5），接著顯示每個月的存款總額。

提示：四捨五入，輸出浮點數到小數點後第二位。

舉例：
假設您存款$10,000，年收益為5.75%。
過了一個月，存款會是：10000 + 10000 * 5.75 / 1200 = 10047.92
過了兩個月，存款會是：10047.92 + 10047.92 * 5.75 / 1200 = 10096.06
過了三個月，存款將是：10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
以此類推。

3. 輸入輸出：
輸入說明
一個正整數（金額）、一個正數（收益率）及一個正整數（月份）

輸出說明
格式化輸出每個月的存款總額

範例輸入
50000
1.3
5
範例輸出
Month 	  Amount
  1 	 50054.17
  2 	 50108.39
  3 	 50162.68
  4 	 50217.02
  5 	 50271.42
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#==================================================================================

amount = float(input())
annual_rate = float(input())
months = int(input())

print("Month \t  Amount")

for month in range(1, months + 1):
    amount += amount * annual_rate / 1200
    print(f"{month:>3} \t {amount:>8.2f}")
