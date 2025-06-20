# Python 805 字串輸出

TQC+ 程式語言Python 805 字串輸出
最新一次更新時間：2023-05-12 10:18:42

1. 題目說明:
請開啟PYD805.py檔案，依下列題意進行作答，將字串依規則進行輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA805.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入一個長度為6的字串，將此字串分別置於10個欄位的寬度的左邊、中間和右邊，並顯示這三個結果，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
一個長度為6的字串

輸出說明
格式化輸出

範例輸入
python
範例輸出
|python    |
|  python  |
|    python|
程式執行狀況擷圖
下圖中的 粉紅色點 為 空格

Alt text

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=================================================================================

s = input()
print(f"|{s:<10}|")   # 靠左對齊
print(f"|{s:^10}|")   # 置中對齊
print(f"|{s:>10}|")   # 靠右對齊

