# 301P

# 1
num_values = int(input("입력할 값의 개수: "))

values = []


for _ in range(num_values):
    value = int(input())
    values.append(value)


sum_values = sum(values)

print("값의 합계 =", sum_values)