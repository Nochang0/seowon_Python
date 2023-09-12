# 266P
# 2번쨰로 큰 수 찾기 프로그램

# 1
list1 = [1, 2, 3, 4, 15, 99]
list1.sort()
print("두 번쨰로 큰 수=", list1[-2])

# 2
list1 = [1, 2, 3, 4, 15, 99]
list1.remove(max(list1))
print("두 번쨰로 큰 수=", max(list1))