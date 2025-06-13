# Python 701 串列數組轉換

TQC+ 程式語言Python 701 串列數組轉換
最新一次更新時間：2019-04-16 03:33:42

1. 題目說明:
請開啟PYD701.py檔案，依下列題意進行作答，將串列轉為數組，使輸出值符合題意要求。作答完成請另存新檔為PYA701.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。

3. 輸入輸出：
輸入說明
n個整數，直至-9999結束輸入

輸出說明
數組
數組的長度
數組中的最大值
數組中的最小值
數組內的整數總和

範例輸入
-4
0
37
19
26
-43
9
-9999
範例輸出
(-4, 0, 37, 19, 26, -43, 9)
Length: 7
Max: 37
Min: -43
Sum: 44
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#===================================================================================

import sys

# 讀取輸入
nums = []
for line in sys.stdin:
    num = int(line.strip())
    if num == -9999:
        break
    nums.append(num)

# 轉換為數組（Tuple）
nums_tuple = tuple(nums)

# 輸出結果
print(nums_tuple)
print(f"Length: {len(nums_tuple)}")
print(f"Max: {max(nums_tuple)}")
print(f"Min: {min(nums_tuple)}")
print(f"Sum: {sum(nums_tuple)}")
