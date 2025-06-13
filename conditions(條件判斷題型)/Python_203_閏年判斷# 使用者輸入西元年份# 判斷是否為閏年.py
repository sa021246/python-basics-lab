# Python 203 閏年判斷

# 使用者輸入西元年份
year = int(input())

# 判斷是否為閏年
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

