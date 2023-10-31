# 7과 4번

dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

key = input("키를 입력하시오: ")

if int(key) in dictionary:
    print("키", key, "은(는) 딕셔너리에 있습니다.")
else:
    print("키", key, "은(는) 딕셔너리에 없습니다.")