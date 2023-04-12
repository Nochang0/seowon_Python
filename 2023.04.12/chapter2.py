# 챕터2 110P ~ 112P 홀수 문제

# 1
x = int(input("x: "))
y = int(input("y: "))

print("두수의 합: ", x+y)
print("두수의 차: ", x-y)
print("두수의 곱: ", x*y)
print("두수의 평균: ", (x+y)/2)
print("큰수: ", max(x, y))
print("작은수: ", min(x, y))

# 3
x = int(input("삼각형의 밑변: "))
y = int(input("삼각형의 높이: "))

print("삼각형의 나머지 변의 최대 길이: ", int((x+y)-1))

# 5
ftemp = int(input("화씨 온도를 입력하시오: "))
ctemp = (ftemp-32)*5.0/9.0
print("화씨", ftemp, "도는 섭씨",ctemp, "도 에 해당합니다.") 

# 7
x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
dist = ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
print("두점 사이의 거리= ", dist)

# 9
n = int(input("정수="))
s = 0
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
s += n % 10
n //= 10
print(s)

# 11
# 11
drive_name = input("드라이브 이름: ")
directory_name = input("디렉토리 이름: ")
file_name = input("파일 이름: ")
extension_name = input("확장자: ")

full_file_name = drive_name + ":" + directory_name + file_name + "." + extension_name

print("완전한 파일 이름은 다음과 같습니다: " + full_file_name)