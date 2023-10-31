# 7과 9번


str1 = input("첫 번째 문자열을 입력하세요: ")
str2 = input("두 번째 문자열을 입력하세요: ")

# 두 문자열에 공통으로 포함된 글자를 찾습니다.
common_characters = ""

for char in str1:
    if char in str2 and char not in common_characters:
        common_characters += char

# 결과 출력
if common_characters:
    print("두 문자열에 공통으로 포함된 글자:", common_characters)
else:
    print("두 문자열에 공통으로 포함된 글자가 없습니다.")