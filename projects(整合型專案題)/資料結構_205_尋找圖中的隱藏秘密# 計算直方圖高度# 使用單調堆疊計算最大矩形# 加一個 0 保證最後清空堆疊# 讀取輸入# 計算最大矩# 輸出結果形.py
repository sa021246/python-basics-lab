# 資料結構 205 尋找圖中的隱藏秘密

TQC+ 程式設計：資料結構 205 尋找圖中的隱藏秘密
最新一次更新時間：2024-05-08 10:26:00

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 在一個古老的科學研究所中，研究員發現了一張神秘的二維二元圖像，這張圖像只包含黑色（由 0 組成）和白色（由 1 組成）。

(2) 據說，這個圖像中隱藏著一個重要的秘密：「最大的連續白色矩形區域（由 1 組成）」代表著一個神秘代碼的位置。為了解開這個秘密，研究員需要編寫一個程式來尋找這個「最大的連續白色矩形區域」。

提示：「最大的連續白色矩形區域」即為「最大矩形」，而且圖中只有唯一一個，其面積為組成該區域數字「1」的總數。

提示：程式由左至右，由上至下找尋。

3. 輸入輸出：
輸入說明
第 1 列：輸入 n、m 兩個正整數，代表二維圖像大小為 n * m。
第 2 ~ n + 1 列：每列輸入 m 個整數序列（由 0 和 1 組成），整數間以半形空白間隔。

輸出說明
第 1 列：輸出最大矩形面積。
第 2 列：輸出最大矩形面積左上角的位置座標。
第 3 列：輸出最大矩形面積右下角的位置座標。

範例輸入1
4 5
0 1 1 1 0
1 1 1 1 0
1 0 1 0 0
1 0 0 0 1
範例輸出1
6
(0, 1)
(1, 3)
範例輸入2
4 6
0 0 1 1 1 0
0 1 1 1 0 0
1 1 0 0 0 0
1 1 1 1 1 0
範例輸出2
5
(3, 0)
(3, 4)
待編修檔案

#==================================================================================

def maximalRectangle(matrix):
    if not matrix:
        return 0, (-1, -1), (-1, -1)

    n, m = len(matrix), len(matrix[0])
    heights = [0] * m
    max_area = 0
    top_left = (0, 0)
    bottom_right = (0, 0)

    for i in range(n):
        for j in range(m):
            # 計算直方圖高度
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        # 使用單調堆疊計算最大矩形
        stack = []
        extended = heights + [0]  # 加一個 0 保證最後清空堆疊

        for idx, h in enumerate(extended):
            while stack and h < extended[stack[-1]]:
                height = extended[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                area = height * width

                if area > max_area:
                    max_area = area
                    end_col = idx - 1
                    start_col = end_col - width + 1
                    end_row = i
                    start_row = i - height + 1
                    top_left = (start_row, start_col)
                    bottom_right = (end_row, end_col)

            stack.append(idx)

    return max_area, top_left, bottom_right


# 讀取輸入
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 計算最大矩形
area, top_left, bottom_right = maximalRectangle(matrix)

# 輸出結果
print(area)
print(f"({top_left[0]}, {top_left[1]})")
print(f"({bottom_right[0]}, {bottom_right[1]})")
