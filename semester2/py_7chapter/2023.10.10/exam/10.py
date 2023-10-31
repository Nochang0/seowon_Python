# 7과 10번

set1 = {10, 20, 30, 40, 50, 60}
set2 = {30, 40, 50, 60, 70, 80}

only_in_set1 = set1 - set2
only_in_set2 = set2 - set1

print("첫 번째 세트", set1)
print("두 번째 세트", set2)
print("어느 한쪽에만 있는 요소들", only_in_set1.union(only_in_set2))