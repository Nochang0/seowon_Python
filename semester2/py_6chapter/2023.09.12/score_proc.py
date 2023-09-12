# 265P 
# 성적 처리 프로그램

STDENTS = 5
lst = []
count = 0

for i in range(STDENTS):
    value = int(input("성적을 입력하시오: "))
    lst.append(value)
    
print("\n성적 평균=", sum(lst) / len(lst))
print("\n최대점수=", max(lst))
print("\n최소점수=", min(lst))