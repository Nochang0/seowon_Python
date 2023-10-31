# 7과 1번

input_str = input("정수 리스트를 입력하세요 (쉼표로 구분하여): ")
input_list = input_str.split(",")

# 입력된 문자열을 정수 리스트로 변환
try:
    int_list = [int(item) for item in input_list]
except ValueError:
    print("올바른 정수 리스트 형식이 아닙니다.")
    exit(1)

# 중복된 요소 제거 및 정렬
unique_sorted_list = sorted(list(set(int_list)))

# 결과 출력
print("중복 제거 및 정렬된 리스트:")
for item in unique_sorted_list:
    print(item)