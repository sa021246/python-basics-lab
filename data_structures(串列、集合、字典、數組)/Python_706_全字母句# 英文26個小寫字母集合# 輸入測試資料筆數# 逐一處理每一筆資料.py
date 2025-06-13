# Python 706 全字母句

TQC+ 程式語言Python 706 全字母句
最新一次更新時間：2019-04-16 03:37:17

1. 題目說明:
請開啟PYD706.py檔案，依下列題意進行作答，進行全字母句之判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA706.py再進行評分。

2. 設計說明：
全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）。

提示：不區分大小寫字母

3. 輸入輸出：
輸入說明
先輸入一個正整數表示測試資料筆數，再輸入測試資料

輸出說明
輸入的資料是否為全字母句

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
3
The quick brown fox jumps over the lazy dog
True
Learning Python is funny
False
Pack my box with five dozen liquor jugs
True

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
2
Quick fox jumps nightly above wizard
True
These can be weapons of terror
False

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#==================================================================================

# PYA706.py

# 英文26個小寫字母集合
alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

# 輸入測試資料筆數
k = int(input())

# 逐一處理每一筆資料
for _ in range(k):
    sentence = input().lower()  # 轉小寫以忽略大小寫差異
    # 將句子中的字母轉為集合，並與 alphabet_set 做子集合比較
    sentence_letters = set(filter(str.isalpha, sentence))
    print(sentence_letters >= alphabet_set)
