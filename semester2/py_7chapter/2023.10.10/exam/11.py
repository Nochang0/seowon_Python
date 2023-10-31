# 7과 11번

questions = "다음은 어떤 단어에 대한 설명일까요?\n최근에 가장 떠오르는 프로그래밍 언어\n(1)파이썬 (2)변수 (3)함수 (4)리스트\n\n"
answer = "파이썬"

print(questions)
user_answer = input()

if user_answer == answer:
    print("정답입니다!")
else:
    print("틀렸습니다.")
