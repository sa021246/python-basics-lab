# 資料結構 304 完美拼布

TQC+ 程式設計：資料結構 304 完美拼布
最新一次更新時間：2024-05-08 13:11:45

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 美術老師有 m 塊布料，每一塊布料上面皆印有英文小寫字母組成的字串。若兩塊布料上面的「A字串」和「B字串」連接起來的字串「AB」或「BA」，皆可拆成左右各半且內容完全一樣的子字串，則稱為「完美拼布」。

例如：兩塊布料上面的「A字串」和「B字串」分別為「piep」和「ie」，則連接起來的字串為「piepie」或「iepiep」，皆可以拆成左右各半且內容相同的子字串「pie」、「pie」或「iep」、「iep」，如此符合「完美拼布」的條件。

(2) 現在美術老師有 m 塊布料，請問有幾對布料可以形成「完美拼布」？

提示：相同的兩個字串組合計算一次即可。

3. 輸入輸出：
輸入說明
第 1 列：輸入一個正整數 m（1 ≤ m ≤ 5000），表示有 m 塊布料。
第 2~m+1 列：輸入每一塊布料上的字串，字串皆相異且字串長度不超過1000。

輸出說明
有幾對布料滿足完美拼布的條件。

範例輸入1
3
a
aba
aaa
範例輸出1
1
範例輸入2
5
abyyyab
y
yy
yyy
yyyy
範例輸出2
3
待編修檔案

#================================================================================

def is_perfect_patch(a, b):
    # 檢查 a + b 和 b + a 是否是完美拼布
    for combo in [a + b, b + a]:
        if len(combo) % 2 == 0:
            mid = len(combo) // 2
            if combo[:mid] == combo[mid:]:
                return True
    return False

# 讀取輸入
m = int(input())
fabrics = [input().strip() for _ in range(m)]

count = 0
# 遍歷所有不重複的布料對
for i in range(m):
    for j in range(i + 1, m):
        if is_perfect_patch(fabrics[i], fabrics[j]):
            count += 1

print(count)
