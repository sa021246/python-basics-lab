# 資料結構 305 員工資料查詢

TQC+ 程式設計：資料結構 305 員工資料查詢
最新一次更新時間：2024-05-08 11:16:34

1. 題目說明：
請依下列題意進行作答，使輸出值符合題意要求。

1. 設計說明：
(1) 公司具有以下四張紀錄表：

員工資料表（EMPLOYEE），記錄員工編號（e_id）、員工姓名（e_name）、員工月薪水（e_salary）、員工部門編號（d_id）。

部門資料表（DEPARTMENT），記錄部門編號（d_id）、部門名稱（d_name）、部門經理員工編號（m_id）。

專案資料表（PROJECT），記錄專案編號（p_id）、專案名稱（p_name）、專案地點（p_location）。

員工參與專案時數資料表（HOUR_LOG），記錄員工編號（e_id）、參與專案編號（p_id）、參與專案時數（p_hours）。

(2) 請撰寫一程式，讓使用者輸入上述四種資料，以及某員工姓名（Name），列出該員工所參與的專案名稱（p_name），以及參與該專案的工作時數（p_hours）。

2. 輸入輸出：
輸入說明
第 1 列：四個小於 10 的正整數 E、D、P、H，E 為員工資料筆數、D 為部門資料筆數、P 為專案資料筆數、H 為員工參與專案時數筆數。
第 2 ~ E+1 列：員工資料表（EMPLOYEE），每一列包含員工編號（e_id，4字元）、員工姓名（e_name，3~10字元）、員工月薪水（e_salary，正整數）、員工部門編號（d_id，4字元）；
第 E+2 ~ E+D+1 列：部門資料表（DEPARTMENT），每一列包含部門編號（d_id，4字元）、部門名稱（d_name，3~10字元）、部門經理員工編號（m_id，4字元）；
第 E+D+2 ~ E+D+P+1 列：專案資料表（PROJECT），每一列包含專案編號（p_id，4字元）、專案名稱（p_name，3~10字元）、專案地點（p_location，3~10字元）；
第 E+D+P+2 ~ E+D+P+H+1 列：員工參與專案時數資料表（HOUR_LOG），每一列包含員工編號（e_id，4字元）、參與專案編號（p_id，4字元）、參與專案時數（p_hours，正整數）。
第 E+D+P+H+2 列：欲查詢的員工姓名。

（注意：所有資料間皆以一個半形空白間隔。）

輸出說明
該員工所參與的專案名稱（p_name），以及參與該專案的工作時數（p_hours），資料間皆以一個半形空白間隔，輸出順序請依照專案名稱字典順序「由小到大」。
最後輸出該員工參與專案的總時數。

範例輸入1
3 2 2 4
E001 John 45000 D001
E002 Mary 43000 D002
E003 Tom 46000 D002
D001 RD E001
D002 SALE E002
P001 AI Taipei
P002 SE Tainan
E001 P001 20
E002 P002 30
E003 P001 20
E002 P001 10
Mary
範例輸出1
AI 10
SE 30
40
範例輸入2
4 3 4 7
E001 John 45000 D001
E002 Mary 43000 D002
E003 Tom 46000 D002
E004 Jame 50000 D003
D001 RD E001
D002 SALE E002
D003 Product E004
P001 AI Taipei
P002 SE Tainan
P003 IMG UK
P004 WEB Taipei
E001 P001 20
E004 P004 20
E002 P002 30
E004 P002 20
E003 P001 20
E002 P001 10
E004 P003 20
Jame
範例輸出2
IMG 20
SE 20
WEB 20
60
待編修檔案

#=================================================================================

# 讀取資料筆數
E, D, P, H = map(int, input().split())

# 讀取員工資料 EMPLOYEE
employee = {}
name_to_id = {}
for _ in range(E):
    e_id, e_name, e_salary, d_id = input().split()
    employee[e_id] = {
        "name": e_name,
        "salary": int(e_salary),
        "d_id": d_id
    }
    name_to_id[e_name] = e_id

# 讀取部門資料 DEPARTMENT（本題不使用，可略過）
for _ in range(D):
    input()

# 讀取專案資料 PROJECT
project = {}
for _ in range(P):
    p_id, p_name, p_location = input().split()
    project[p_id] = p_name

# 讀取參與專案資料 HOUR_LOG
hour_log = []
for _ in range(H):
    e_id, p_id, p_hours = input().split()
    hour_log.append({
        "e_id": e_id,
        "p_id": p_id,
        "p_hours": int(p_hours)
    })

# 讀取要查詢的員工姓名
query_name = input()
query_id = name_to_id.get(query_name)

# 整理該員工的參與專案及時數
project_hours = {}
total_hours = 0

for log in hour_log:
    if log["e_id"] == query_id:
        p_name = project[log["p_id"]]
        project_hours[p_name] = project_hours.get(p_name, 0) + log["p_hours"]
        total_hours += log["p_hours"]

# 根據專案名稱排序輸出
for p_name in sorted(project_hours):
    print(p_name, project_hours[p_name])

print(total_hours)
