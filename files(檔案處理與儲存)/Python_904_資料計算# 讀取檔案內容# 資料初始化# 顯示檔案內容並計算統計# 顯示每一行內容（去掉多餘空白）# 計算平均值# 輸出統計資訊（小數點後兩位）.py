# Python 904 資料計算

TQC+ 程式語言Python 904 資料計算
最新一次更新時間：2019-04-16 03:46:40

1. 題目說明:
請開啟PYD904.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA904.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

範例輸入
無

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
待編修檔案

#================================================================================

# PYA724.py

# 讀取檔案內容
with open("read.txt", "r") as file:
    lines = file.readlines()

# 資料初始化
total_height = 0
total_weight = 0
max_height = 0
max_weight = 0
tallest_person = ""
heaviest_person = ""
count = 0

# 顯示檔案內容並計算統計
for line in lines:
    print(line.strip())  # 顯示每一行內容（去掉多餘空白）
    name, height, weight = line.strip().split()
    height = float(height)
    weight = float(weight)
    total_height += height
    total_weight += weight
    count += 1

    if height > max_height:
        max_height = height
        tallest_person = name

    if weight > max_weight:
        max_weight = weight
        heaviest_person = name

# 計算平均值
avg_height = total_height / count
avg_weight = total_weight / count

# 輸出統計資訊（小數點後兩位）
print(f"Average height: {avg_height:.2f}")
print(f"Average weight: {avg_weight:.2f}")
print(f"The tallest is {tallest_person} with {max_height:.2f}cm")
print(f"The heaviest is {heaviest_person} with {max_weight:.2f}kg")

