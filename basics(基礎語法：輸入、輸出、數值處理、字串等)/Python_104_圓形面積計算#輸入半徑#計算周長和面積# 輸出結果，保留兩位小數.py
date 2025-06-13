# Python 104 圓形面積計算

TQC+ 程式語言Python 104 圓形面積計算
最新一次更新時間：2019-04-16 02:03:09

1. 題目說明:
請開啟PYD104.py檔案，依下列題意進行作答，計算圓形之面積和周長，使輸出值符合題意要求。作答完成請另存新檔為PYA104.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
半徑

輸出說明
半徑
周長
面積

範例輸入1
10
範例輸出1
Radius = 10.00
Perimeter = 62.83
Area = 314.16
範例輸入2
2.5
範例輸出2
Radius = 2.50
Perimeter = 15.71
Area = 19.63
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0

========================================================================

#new===============================================================================

# TODO
import math
radius = eval(input())

# TODO
print("Radius = {:.2f}".format(radius))
print("Perimeter = {:.2f}".format(radius*2*math.pi))
print("Area = {:.2f}".format(radius**2*math.pi))
"""
Radius = _
Perimeter = _
Area = _
"""

=========================================================================

runfile('C:/Users/andyb/Desktop/安納/宏碁/code judge/1/PYD104.py', wdir='C:/Users/andyb/Desktop/安納/宏碁/code judge/1')

10
Radius = 10.00
Perimeter = 62.83
Area = 314.16

runfile('C:/Users/andyb/Desktop/安納/宏碁/code judge/1/PYD104.py', wdir='C:/Users/andyb/Desktop/安納/宏碁/code judge/1')

2.5
Radius = 2.50
Perimeter = 15.71
Area = 19.63

#old===========================================================================

# TODO
import math
radius = eval(input())

PI = math.pi

# TODO
print("Radius = %.2f" % radius)
print("Perimeter = %.2f" % (radius*2*PI))
print("Area = %.2f"%(radius**2*PI))

=========================================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 106 整數格式化輸出/PYD106.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 106 整數格式化輸出')

10
Radius = 10.00
Perimeter = 62.83
Area = 314.16

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 106 整數格式化輸出/PYD106.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 106 整數格式化輸出')

2.5
Radius = 2.50
Perimeter = 15.71
Area = 19.63
