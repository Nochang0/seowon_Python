# 202311420 연승현
# 248P 14번


def sqrt(x, guess):
    if abs(x/guess - guess) < 0.0001: # 거의 동일한 경우
        return guess
    else: # 새로운 추측값 계산
        new_guess = (guess + x/guess) / 2
        return sqrt(x, new_guess)

print(sqrt(2,1)) # 1.4142