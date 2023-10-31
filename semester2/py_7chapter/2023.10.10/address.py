# 333P

def main():
    address_book = {}
    while True :
        user = display_menu();
        if user == 1:
            name, number = get_contact()
            address_book[name] = number
        elif user == 2:
            name, number = get_contact()
            address_book.pop(name)
        elif user == 3:
            pass
        elif user == 4:
            for key in sorted(address_book):
                print(key, "의 전화번호:", address_book[key])
        else:
            break
            
def get_contact():
    name = input("이름: ")
    number = input("전화번호: ")
    return name, number

def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

main()