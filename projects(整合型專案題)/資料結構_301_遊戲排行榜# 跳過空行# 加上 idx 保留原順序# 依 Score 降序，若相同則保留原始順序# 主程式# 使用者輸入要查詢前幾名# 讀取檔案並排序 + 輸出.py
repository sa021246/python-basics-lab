# 資料結構 301 遊戲排行榜

TQC+ 程式設計：資料結構 301 遊戲排行榜
最新一次更新時間：2024-05-08 10:37:06

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 小林想要在多人線上角色扮演遊戲（MMORPG）中加入一個排行榜介面的功能，這個排行榜要能依遊戲積分（Score）由高到低進行排序。

(2) 請讀取角色資料 read.csv 檔案，角色資料欄位說明如下：

Id：角色的不重複ID
Name：角色的英文名稱
Level：角色的等級
Score：角色的遊戲積分
請依遊戲積分「由高到低」排序，最後輸出指定數量的排名列表（若有相同積分情況，則依原始輸入順序呈現即可）。

提示：read.csv 檔案內容為簡易CSV檔，文字內容為純英文數字、半形逗號，不包含跳脫字元，亦無使用雙引號，每一列皆可單純使用半形逗號（,）做欄位分隔。

提示：可使用快速排序（Quick Sort）或合併排序（Merge Sort）來實作排序邏輯。

3. 輸入輸出：
輸入說明
一個正整數 n。

輸出說明
遊戲積分「由高到低」的 n 筆角色排行列表，依序包含 Rank、Id、Name、Level 與 Score。

若 n 超過資料總量，則不顯示任何角色資料，直接輸出「Exceeds data upper limit」。

註：

Rank 為排名流水號，從 1 開始。
資料間使用半形空白與垂直線「 | 」間隔。
範例輸入1
3
範例輸出1
1 | 209 | Iris | 88 | 6048
2 | 789 | William | 91 | 5567
3 | 461 | Noah | 89 | 3045
範例輸入2
5
範例輸出2
1 | 209 | Iris | 88 | 6048
2 | 789 | William | 91 | 5567
3 | 461 | Noah | 89 | 3045
4 | 759 | Chloe | 58 | 2675
5 | 265 | Scarlett | 17 | 1973
待編修檔案

#==================================================================================

def read_csv_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for idx, line in enumerate(lines):
        line = line.strip()
        if line:  # 跳過空行
            parts = line.split(',')
            id_, name, level, score = parts
            data.append((idx, int(id_), name, int(level), int(score)))  # 加上 idx 保留原順序
    return data

def sort_and_output(data, n):
    if n > len(data):
        print("Exceeds data upper limit")
        return
    # 依 Score 降序，若相同則保留原始順序
    sorted_data = sorted(data, key=lambda x: (-x[4], x[0]))

    for rank, entry in enumerate(sorted_data[:n], 1):
        _, id_, name, level, score = entry
        print(f"{rank} | {id_} | {name} | {level} | {score}")

# 主程式
n = int(input())  # 使用者輸入要查詢前幾名

# 讀取檔案並排序 + 輸出
filename = 'read.csv'
data = read_csv_data(filename)
sort_and_output(data, n)
