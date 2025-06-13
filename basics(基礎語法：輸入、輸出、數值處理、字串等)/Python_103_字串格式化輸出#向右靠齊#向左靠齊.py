# Python 103 字串格式化輸出

TQC+ 程式語言Python 103 字串格式化輸出
最新一次更新時間：2019-04-16 02:02:30

1. 題目說明:
請開啟PYD103.py檔案，依下列題意進行作答，輸入單字及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA103.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個單字

輸出說明
格式化輸出

範例輸入
I
enjoy
learning
Python
範例輸出
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

========================================================================================

#new==========================================================

#I:

wordA = str(input())

wordB = str(input())

wordC = str(input())

wordD = str(input())


#P:





#O:

# 向右靠
print("|{0:>10s} {1:>10s}|".format(wordA, wordB))

print("|{0:>10s} {1:>10s}|".format(wordC, wordD))

# 向左靠
print("|{0:10s} {1:10s}|".format(wordA, wordB))

print("|{0:10s} {1:10s}|".format(wordC, wordD))

=======================================================================================

runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 103 字串格式化輸出/PYD103.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 103 字串格式化輸出')

I

enjoy

learning

Python
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |

#old============================================================================

#I:

wordA = str(input())

wordB = str(input())

wordC = str(input())

wordD = str(input())


#P:





#O:

# 向右靠
print("|%10s %10s|"%(wordA, wordB))

print("|%10s %10s|"%(wordC, wordD))

# 向左靠
print("|%-10s %-10s|"%(wordA, wordB))

print("|%-10s %-10s|"%(wordC, wordD))

=======================================================================================
runfile('D:/我的書桌/code judge/TQC+ 程式語言Python 103 字串格式化輸出/PYD103.py', wdir='D:/我的書桌/code judge/TQC+ 程式語言Python 103 字串格式化輸出')

I

enjoy

learning

Python
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |


