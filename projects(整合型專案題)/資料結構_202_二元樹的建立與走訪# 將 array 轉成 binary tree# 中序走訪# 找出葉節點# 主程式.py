# 資料結構 202 二元樹的建立與走訪

TQC+ 程式設計：資料結構 202 二元樹的建立與走訪
最新一次更新時間：2024-05-08 09:46:45

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 撰寫程式讓使用者輸入一個以陣列（Array）表示完全二元樹（Complete Binary Tree）的字串，例如：「A,B,C,D,,E,F」，其中節點（Node）以大寫英文字母表示，且節點與節點間以半形逗號（,）隔開，轉換方式如下圖。

輸入字串轉換為二元樹

(2) 針對轉換後的二元樹，請以中序走訪（Inorder）依序輸出所有節點，並按照「字母順序」輸出此二元樹的所有葉節點（Leaf node）。

提示：節點數量小於 20 個。

3. 輸入輸出：
輸入說明
一個代表完全二元樹的字串，節點以大寫英文字母表示，且節點與節點間以半形逗號（,）間隔。

輸出說明
第 1 列：以中序走訪依序輸出所有節點。
第 2 列：依照「字母順序」輸出此二元樹的所有葉節點。

範例輸入1
A,B,C,D,,E,F
範例輸出1
DBAECF
DEF
範例輸入2
A,B,C,D,E,,,,,F,G
範例輸出2
DBFEGAC
CDFG
待編修檔案

#================================================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 將 array 轉成 binary tree
def build_tree(nodes):
    tree_nodes = []
    for val in nodes:
        tree_nodes.append(TreeNode(val) if val != '' else None)

    for i in range(len(nodes)):
        if tree_nodes[i]:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                tree_nodes[i].left = tree_nodes[left_index]
            if right_index < len(nodes):
                tree_nodes[i].right = tree_nodes[right_index]
    return tree_nodes[0] if tree_nodes else None

# 中序走訪
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.val)
        inorder_traversal(node.right, result)

# 找出葉節點
def find_leaves(node, leaves):
    if node:
        if not node.left and not node.right:
            leaves.append(node.val)
        find_leaves(node.left, leaves)
        find_leaves(node.right, leaves)

# 主程式
input_str = input().strip()
arr = input_str.split(",")

root = build_tree(arr)

inorder_result = []
inorder_traversal(root, inorder_result)
print(''.join(inorder_result))

leaf_nodes = []
find_leaves(root, leaf_nodes)
print(''.join(sorted(leaf_nodes)))
