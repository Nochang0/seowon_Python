##
# 이 프로그램은 사용자로부터 이름과 나이를 받아서 다시 출력한다.
# 227P

def get_info():
    name = input("이름:")
    age = int(input("나이:"))
    return name, age

st_name, st_age = get_info()
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")
