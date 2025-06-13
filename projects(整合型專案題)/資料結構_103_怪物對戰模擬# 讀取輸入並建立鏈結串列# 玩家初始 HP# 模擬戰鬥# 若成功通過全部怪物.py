# 資料結構 103 怪物對戰模擬

TQC+ 程式設計：資料結構 103 怪物對戰模擬
最新一次更新時間：2024-05-08 13:05:06

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 小林正在設計一個與怪物連續對戰的遊戲程式。程式讓使用者輸入一個正整數序列，代表此關卡會出現的怪物數量與其攻擊力。例如：輸入「10,20,30」，每個數字分別代表每隻怪物的攻擊力，數字之間用半形逗號（,）隔開，若輸入 n 個數字代表總共有 n 隻怪物。

(2) 請使用鏈結串列的方式，依序初始化此怪物序列。

(3) 遊戲玩家角色的 HP 血量預設為 100，玩家會從頭輪詢怪物序列，每經過一個怪物節點就扣除相對應的 HP 血量，直到玩家的 HP ≤ 0。

3. 輸入輸出：
輸入說明
一個正整數序列，代表怪物數量與其攻擊力。

輸出說明
若玩家成功通過所有怪物，輸出「game clear! hp left (剩餘血量)」。
否則，輸出「game over! dead at level (第幾回合死亡)」。

範例輸入1
10,20,30
範例輸出1
game clear! hp left 40
範例輸入2
50,50
範例輸出2
game over! dead at level 2
待編修檔案

#================================================================================

class MonsterNode:
    def __init__(self, attack):
        self.attack = attack
        self.next = None

# 讀取輸入並建立鏈結串列
data = input().split(',')
head = None
tail = None

for value in data:
    node = MonsterNode(int(value))
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

# 玩家初始 HP
hp = 100
level = 0
current = head

# 模擬戰鬥
while current:
    level += 1
    hp -= current.attack
    if hp <= 0:
        print(f"game over! dead at level {level}")
        break
    current = current.next

# 若成功通過全部怪物
if hp > 0:
    print(f"game clear! hp left {hp}")
