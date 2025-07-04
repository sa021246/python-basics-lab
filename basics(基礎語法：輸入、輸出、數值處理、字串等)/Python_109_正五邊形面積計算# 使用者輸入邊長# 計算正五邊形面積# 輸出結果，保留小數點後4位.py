# Python 109 正五邊形面積計算

TQC+ 程式語言Python 109 正五邊形面積計算
最新一次更新時間：2022-08-19 11:28:41

1. 題目說明:
請開啟PYD109.py檔案，依下列題意進行作答，計算正五邊形之面積，使輸出值符合題意要求。作答完成請另存新檔為PYA109.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正五邊形面積的公式： 
提示3：輸出浮點數到小數點後第四位。

3. 輸入輸出：
輸入說明
正數s

輸出說明
正五邊形面積

範例輸入
5
範例輸出
Area = 43.0119
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
======================================================================================================================

#new==============================================================================

import math

PI = math.pi

POW = math.pow

TAN = math.tan

#I:

s = eval(input())

#P:

area = (5*s**2)/(4*TAN(PI/5))


#O:

print("Area = {:.4f}".format(area))

===========================================================(答案正確)

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 109 正五邊形面積計算/PYD109.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 109 正五邊形面積計算')

5
Area = 43.0119


#old=================================================================================

import math

PI = math.pi

POW = math.pow

TAN = math.tan

#I:

s = eval(input())

#P:

area = (5*s**2)/(4*TAN(PI/5))


#O:

print("Area = %.4f"%area)

===========================================================(答案正確)

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 109 正五邊形面積計算/PYD109.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 109 正五邊形面積計算')

5
Area = 43.0119
