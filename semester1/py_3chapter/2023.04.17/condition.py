# 126P

x = int(input("첫 번째 수 = "))
y = int(input("두 번째 수 = "))

max_value = (x if x > y else y)
min_value = (y if x > y else x)

print("큰 수 =", max_value, "작은 수 =", min_value)