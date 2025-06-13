# Python 107 數值計算

TQC+ 程式語言Python 107 數值計算
最新一次更新時間：2019-04-16 02:04:22

1. 題目說明:
請開啟PYD107.py檔案，依下列題意進行作答，計算五個數字之數值、總和及平均數，使輸出值符合題意要求。作答完成請另存新檔為PYA107.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。

提示：總和與平均數皆輸出到小數點後第1位。

3. 輸入輸出：
輸入說明
五個數字

輸出說明
輸出五個數字
總和
平均數

範例輸入1
20
40
60
80
100
範例輸出1
20 40 60 80 100
Sum = 300.0
Average = 60.0
範例輸入2
88.7
12
56
132.55
3
範例輸出2
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

=========================================================

#new===============================================================================

#I:
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

#P:

sum = num1+ num2+ num3+ num4+ num5
average = sum/5


#O:

print("{} {} {} {} {}".format(num1, num2, num3, num4, num5))

print("Sum = {:.1f}".format(sum))

print("Average = {:.1f}".format(average))

====================================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算/PYD107.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算')

88.7

12

56

132.55

3
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5


#old=================================================================================

#I:
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

#P:

sum = num1+ num2+ num3+ num4+ num5
average = sum/5


#O:

print("%s %s %s %s %s"%num1, num2, num3, num4, num5)

print("Sum = %.1f"%sum)

print("Average = %.1f"%average)

====================================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算/PYD107.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算')

20

40

60

80

100
20 40 60 80 100
Sum = 300.0
Average = 60.0

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算/PYD107.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 107 數值計算')

88.7

12

56

132.55

3
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5
