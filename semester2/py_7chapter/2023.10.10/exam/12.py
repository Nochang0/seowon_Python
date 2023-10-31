# 7과 12번

text = input("문자열을 입력하시오: ")
censored_words = input("금칙어를 입력하시오: ").split()

for word in censored_words:
    text = text.replace(word, '*' * len(word))

print(text)
