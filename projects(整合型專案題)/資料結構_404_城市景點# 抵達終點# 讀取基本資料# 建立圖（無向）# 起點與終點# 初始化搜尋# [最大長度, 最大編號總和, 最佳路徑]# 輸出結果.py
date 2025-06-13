# 資料結構 404 城市景點


TQC+ 程式設計：資料結構 404 城市景點
最新一次更新時間：2024-06-06 16:43:00

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 城市中有 N 個景點（編號為 0 ~ N-1），與 M 條雙向通行的道路，且每一條道路連結兩個景點。

(2) 請撰寫一個程式，讓使用者輸入 M 條連接任兩景點道路資料，找出從景點編號 S 到景點編號 E 所有可能的路徑中，經過景點個數最多的一條路徑（每一條路徑不能重複經過相同景點）。

(3) 若景點個數最多的路徑超過一條，則取景點編號加總最大的路徑。

提示：請使用圖結構搜尋所有路徑。

3. 輸入輸出：
輸入說明
第 1 列：兩個正整數 N、M，其中 N 為景點個數、M 為道路個數。
第 2~M+1 列：每列皆有兩個自然數，為該條道路連接的兩景點編號，共 M 條。
第 M+2 列：兩個自然數 S、E，其中 S 為起始景點編號、E 為結束景點編號。

（所有自然數之間，皆以一個半形空白間隔）

輸出說明
經過景點個數最多的路徑景點編號，編號間以一個半形空白間隔。
（若景點數最多的路徑超過一條，則取景點編號加總最大的路徑）

範例輸入1
6 9
0 1
0 2
0 3
0 4
1 4
2 4
3 4
3 5
4 5
0 5
範例輸出1
0 2 4 3 5
範例輸入2
4 4
0 1
0 2
1 3
2 3
1 3
範例輸出2
1 0 2 3
待編修檔案

#==================================================================================

def dfs(current, path, visited):
    # 抵達終點
    if current == end:
        length = len(path)
        total = sum(path)
        if length > best[0]:
            best[0], best[1], best[2] = length, total, list(path)
        elif length == best[0] and total > best[1]:
            best[1], best[2] = total, list(path)
        return

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            dfs(neighbor, path, visited)
            path.pop()
            visited[neighbor] = False

# 讀取基本資料
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

# 建立圖（無向）
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 起點與終點
start, end = map(int, input().split())

# 初始化搜尋
visited = [False] * N
visited[start] = True
best = [0, 0, []]  # [最大長度, 最大編號總和, 最佳路徑]
dfs(start, [start], visited)

# 輸出結果
print(' '.join(map(str, best[2])))