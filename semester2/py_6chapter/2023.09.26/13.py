# 301P

# 13

seats = [[0] * 10 for _ in range(10)]

print("---------------------")
print("1 2 3 4 5 6 7 8 9 10")
print("---------------------")
for row in seats:
    print(" ".join(str(seat) for seat in row))

while True:
    row_number = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1): "))
    
    if row_number == -1:
        break
    
    col_number = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1): "))
    
    if col_number == -1:
        break
    
    if seats[row_number-1][col_number-1] == 0:
        seats[row_number-1][col_number-1] = 1
        print("예약되었습니다.")
        print("---------------------")
        print("1 2 3 4 5 6 7 8 9 10")
        print("---------------------")
        for row in seats:
            print(" ".join(str(seat) for seat in row))
    else:
        print("이미 예약된 좌석입니다.")
