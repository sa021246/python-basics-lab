# 資料結構 401 圖形的表示與儲存

TQC+ 程式設計：資料結構 401 圖形的表示與儲存
最新一次更新時間：2024-05-08 11:23:56

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 撰寫程式讓使用者讀取一個以相鄰矩陣（Adjacency Matrix）表示圖形（Graph）的 read.txt 檔案，檔案內容與轉換方式如下圖。

以相鄰矩陣表示圖形

(2) read.txt 檔案內儲存的是一個無向（Undirected）且邊有權重（Weighted）的對稱矩陣圖形，請依編號順序（1,2,3,...）輸出所有節點（Vertex）的分支度（Degree），並輸出與各節點相連邊的權重總和中，最大與最小的差。

提示：節點數量小於 10 個。

提示：邊的權重應為大於 0 的正整數；若為 0，則代表無此邊。

3. 輸入輸出：
輸入說明
讀取 read.txt 檔案內容。

輸出說明
第 1 列：依照編號順序（1,2,3,...）輸出所有節點的分支度，各分支度間請使用半形逗號（,）間隔。
第 2 列：輸出與各節點相連邊的權重總和中，最大與最小的差。

範例輸入1
範例輸入1

範例輸出1
Degree:2,4,3,2,3
8
範例輸入2
範例輸入2

範例輸出2
Degree:1,4,2,5,2,2,3,1
17
待編修檔案

#=====================================================================================

def main():
    with open("read.txt", "r") as f:
        matrix = [list(map(int, line.strip().split())) for line in f if line.strip()]
    
    degrees = []
    weight_sums = []
    
    for row in matrix:
        degree = sum(1 for weight in row if weight > 0)
        total_weight = sum(row)
        degrees.append(degree)
        weight_sums.append(total_weight)

    print("Degree:" + ",".join(map(str, degrees)))
    print(max(weight_sums) - min(weight_sums))

if __name__ == "__main__":
    main()
