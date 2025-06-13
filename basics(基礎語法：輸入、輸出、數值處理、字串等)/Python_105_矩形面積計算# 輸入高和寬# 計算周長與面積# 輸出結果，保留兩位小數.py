# Python 105 矩形面積計算

TQC+ 程式語言Python 105 矩形面積計算
最新一次更新時間：2019-04-16 02:03:30

1. 題目說明:
請開啟PYD105.py檔案，依下列題意進行作答，計算矩形之面積和周長，使輸出值符合題意要求。作答完成請另存新檔為PYA105.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
高、寬

輸出說明
高
寬
周長
面積

範例輸入
23.5
19
範例輸出
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

==========================================================

#new===============================================================================

#I:

height = float(input())

width = float(input())

#P:

perimeter = (height + width)*2

area = height * width


#O:

print("Height = {:.2f}".format(height))

print("Width = {:.2f}".format(width))

print("Perimeter = {:.2f}".format(perimeter))

print("Area = {:.2f}".format(area))

============================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 105 矩形面積計算/PYD105.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 105 矩形面積計算')

23.5

19
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50

#old=================================================================================


#I:

height = float(input())

width = float(input())

#P:

perimeter = (height + width)*2

area = height * width


#O:

print("Height = %.2f"%height)

print("Width = %.2f"%width)

print("Perimeter = %.2f"%perimeter)

print("Area = %.2f"%area)

============================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 105 矩形面積計算/PYD105.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 105 矩形面積計算')

23.5

19
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
