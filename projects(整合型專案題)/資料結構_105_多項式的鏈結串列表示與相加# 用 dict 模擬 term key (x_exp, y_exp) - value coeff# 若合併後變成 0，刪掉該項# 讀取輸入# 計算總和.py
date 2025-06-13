# 資料結構 105 多項式的鏈結串列表示與相加

TQC+ 程式設計：資料結構 105 多項式的鏈結串列表示與相加
最新一次更新時間：2024-05-08 14:49:26

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

2. 設計說明：
(1) 一個二元多項式是由多個項組成的，每個項包含三個整數：係數、x 的指數和 y 的指數。需要使用鏈結串列（Linked list）來實作這個多項式的儲存和操作，並完成以下功能：

多項式的鏈結表示：每個節點（或稱為「項」）應包含係數 a、x 的指數 b 和 y 的指數 c，以及指向下一個節點的指針。每一項定義如下：

多項式是由多個「項」組合而成，當使用者輸入一列整數資料代表一個多項式，其中每三個整數代表「一項」。如果新項的 x 和 y 指數已經存在於多項式中，則應將它們的係數相加。

例如：輸入「4 4 0 -5 2 1 2 2 1」，代表為多項式：

多項式相加：實作一個方法來相加兩個多項式，並返回一個新的多項式作為結果。

格式化輸出：輸出結果先依照 x 的指數降冪排序，再依照 y 的指數降冪排序。如果係數是負數，則其前面不應顯示加號。

提示：請利用鏈結串列（Linked list）來實作，有指標的程式語言可利用指標方式實作，有物件導向的程式語言可利用類別來實作。

3. 輸入輸出：
輸入說明
第 1 列：輸入一個正整數 N（2 ≤ N ≤ 10），代表有 N 個二元多項式相加。
第 2~N+1 列：每一列代表一個多項式，每一項有三個整數 a、b、c，所有整數間以一個半形空白間隔。若有 M 組 a、b、c 代表多項式有 M 項。

輸出說明
逐列呈現 N 個二元多項式，並計算所有多項式相加的結果。

註：

多項式的呈現順序，先以 x 的指數降冪排序，再以 y 的指數降冪排序。
次方請以「^」符號表示。例如： 則顯示「10x^5y^4+3x^5y^1-6x^4y^4+1x^3y^0」。
若係數為負數，則其前面不應顯示加號；若係數為 0，則不顯示該項；若係數非 0，則一律顯示係數值。
範例輸入1
2
3 2 1 -4 1 3 8 0 0
7 2 1 -2 1 4 5 1 3
範例輸出1
3x^2y^1-4x^1y^3+8x^0y^0
7x^2y^1-2x^1y^4+5x^1y^3
Sum:10x^2y^1-2x^1y^4+1x^1y^3+8x^0y^0
範例輸入2
3
1 1 0 5 4 3 2 1 0
3 3 3 2 2 2 -1 1 0
3 2 1 -1 1 0 1 0 0 3 0 0
範例輸出2
5x^4y^3+3x^1y^0
3x^3y^3+2x^2y^2-1x^1y^0
3x^2y^1-1x^1y^0+4x^0y^0
Sum:5x^4y^3+3x^3y^3+2x^2y^2+3x^2y^1+1x^1y^0+4x^0y^0
待編修檔案

#=================================================================================

class Term:
    def __init__(self, coeff, x_exp, y_exp):
        self.coeff = coeff
        self.x_exp = x_exp
        self.y_exp = y_exp

    def key(self):
        return (self.x_exp, self.y_exp)

    def __repr__(self):
        return f"{self.coeff}x^{self.x_exp}y^{self.y_exp}"


class Polynomial:
    def __init__(self):
        # 用 dict 模擬 term key: (x_exp, y_exp) -> value: coeff
        self.terms = {}

    def add_term(self, coeff, x_exp, y_exp):
        key = (x_exp, y_exp)
        if key in self.terms:
            self.terms[key] += coeff
        else:
            self.terms[key] = coeff

        # 若合併後變成 0，刪掉該項
        if self.terms[key] == 0:
            del self.terms[key]

    def merge(self, other):
        for (x_exp, y_exp), coeff in other.terms.items():
            self.add_term(coeff, x_exp, y_exp)

    def to_sorted_list(self):
        return sorted(
            [Term(c, x, y) for (x, y), c in self.terms.items()],
            key=lambda term: (-term.x_exp, -term.y_exp)
        )

    def __str__(self):
        term_list = self.to_sorted_list()
        if not term_list:
            return "0"
        output = ""
        for i, t in enumerate(term_list):
            sign = "" if i == 0 or t.coeff < 0 else "+"
            output += f"{sign}{t.coeff}x^{t.x_exp}y^{t.y_exp}"
        return output


# 讀取輸入
N = int(input())
polynomials = []

for _ in range(N):
    data = list(map(int, input().split()))
    poly = Polynomial()
    for i in range(0, len(data), 3):
        a, b, c = data[i], data[i+1], data[i+2]
        poly.add_term(a, b, c)
    polynomials.append(poly)
    print(poly)

# 計算總和
result = Polynomial()
for poly in polynomials:
    result.merge(poly)

print("Sum:" + str(result))
