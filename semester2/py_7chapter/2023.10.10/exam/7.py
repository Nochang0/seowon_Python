# 7과 7번

schedule = {}

def add_event(date, event):
    if date in schedule:
        schedule[date].append(event)
    else:
        schedule[date] = [event]

def view_events(date):
    if date in schedule:
        print(f"{date}의 일정:")
        for event in schedule[date]:
            print(event)
    else:
        print(f"{date}에 일정이 없습니다.")

while True:
    print("1. 일정 추가")
    print("2. 일정 보기")
    print("3. 종료")
    choice = input("원하는 작업을 선택하세요: ")

    if choice == "1":
        date = input("일정을 추가할 날짜를 입력하세요 (YYYY-MM-DD): ")
        event = input("일정 내용을 입력하세요: ")
        add_event(date, event)
        print("일정이 추가되었습니다.")

    elif choice == "2":
        date = input("일정을 확인할 날짜를 입력하세요 (YYYY-MM-DD): ")
        view_events(date)

    elif choice == "3":
        print("일정 애플리케이션을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다. 다시 시도하세요.")