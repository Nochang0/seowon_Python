# 202311420 연승현
# 248P 13번

import random

def dice_game():
    human = random.randint(1, 6)
    computer = random.randint(1, 6)
    print("인간: 주사위값=", human)
    print("컴퓨터: 주사위값=", computer)
    if human > computer:
        print("인간승리")
    elif human < computer:
        print("컴퓨터승리")
    else:
        print("무승부")

while True:
    print("======= dice_game() 호출 ======")
    dice_game()
    print("====== dice_game() 복귀 ======")
    answer = input("중단할까요? Y/N ")
    if answer == 'Y' or answer == 'y':
        break