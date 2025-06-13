# Python 707 共同科目

TQC+ 程式語言Python 707 共同科目
最新一次更新時間：2019-04-16 03:37:57

1. 題目說明:
請開啟PYD707.py檔案，依下列題意進行作答，輸入X組和Y組各自的科目至集合中並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA707.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。請依序分行顯示(1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。

提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

3. 輸入輸出：
輸入說明
輸入X組和Y組各自的科目至集合，直至end結束輸入

輸出說明
X組和Y組的所有科目
X組和Y組的共同科目
Y組有但X組沒有的科目
X組和Y組彼此沒有的科目（不包含相同科目）

輸入與輸出會交雜如下，輸出的部份以粗體字表示
Enter group X's subjects:
Math
Literature
English
History
Geography
end
Enter group Y's subjects:
Math
Literature
Chinese
Physical
Chemistry
end
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'Physical']
['Literature', 'Math']
['Chemistry', 'Chinese', 'Physical']
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']

4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#=======================================================================================

# PYA707.py

# 輸入 X 組科目
print("Enter group X's subjects:")
x_subjects = set()
while True:
    subject = input()
    if subject == "end":
        break
    x_subjects.add(subject)

# 輸入 Y 組科目
print("Enter group Y's subjects:")
y_subjects = set()
while True:
    subject = input()
    if subject == "end":
        break
    y_subjects.add(subject)

# (1) X 和 Y 所有科目（聯集）
all_subjects = sorted(x_subjects | y_subjects)
print(all_subjects)

# (2) X 和 Y 共同科目（交集）
common_subjects = sorted(x_subjects & y_subjects)
print(common_subjects)

# (3) Y 有但 X 沒有的科目（差集）
y_only_subjects = sorted(y_subjects - x_subjects)
print(y_only_subjects)

# (4) X、Y 彼此沒有的科目（對稱差集）
diff_subjects = sorted(x_subjects ^ y_subjects)
print(diff_subjects)
