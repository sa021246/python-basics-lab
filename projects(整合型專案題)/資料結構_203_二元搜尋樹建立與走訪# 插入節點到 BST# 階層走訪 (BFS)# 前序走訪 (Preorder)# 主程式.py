# 資料結構 203 二元搜尋樹建立與走訪

TQC+ 程式設計：資料結構 203 二元搜尋樹建立與走訪
最新一次更新時間：2024-05-08 13:07:52

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 請撰寫一程式，首先要求使用者輸入正整數 N（1 ≤ N ≤ 30），代表有 N 個節點資料，接著依序輸入 N 個節點資料。每一節點資料是一個正整數數字，且整數間以半形空白間隔。

(2) 請將這些節點建構「二元搜尋樹（Binary Search Tree）」，並將此二元樹分別以「階層（Level-Order）走訪」與「前序（Preorder）走訪」順序輸出數列。

提示：輸出文字中「:」為半形字

3. 輸入輸出：
輸入說明
第 1 列：輸入正整數 N（1 ≤ N ≤ 30）為資料個數。
第 2 列：依序輸入 N 個不重複的正整數，整數間以半形空白間隔。

輸出說明
第 1 列：階層走訪結果，整數間以半形空白間隔。
第 2 列：前序走訪結果，整數間以半形空白間隔。

範例輸入1
5
7 9 2 5 10
範例輸出1
Level-order:7 2 9 5 10
Preorder:7 2 5 9 10
範例輸入2
8
25 31 5 9 18 26 51 99
範例輸出2
Level-order:25 5 31 9 26 51 18 99
Preorder:25 5 9 18 31 26 51 99
待編修檔案

#================================================================================

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 插入節點到 BST
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# 階層走訪 (BFS)
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# 前序走訪 (Preorder)
def preorder_traversal(node, result):
    if node:
        result.append(str(node.val))
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

# 主程式
n = int(input())
nums = list(map(int, input().split()))

root = None
for num in nums:
    root = insert_bst(root, num)

level_result = level_order_traversal(root)
preorder_result = []
preorder_traversal(root, preorder_result)

print("Level-order:" + ' '.join(level_result))
print("Preorder:" + ' '.join(preorder_result))
