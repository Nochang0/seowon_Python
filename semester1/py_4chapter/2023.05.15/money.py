# 173P

TARGET = 2000
money = 1000
year = 0
rate = 0

# 현재 금액이 목표 금액보다 작으면 반복한다.
while money < TARGET :
    money = money + money * rate
    year = year + 1

print(year, "년")


