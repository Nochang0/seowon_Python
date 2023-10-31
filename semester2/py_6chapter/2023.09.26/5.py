# 301P

# 5

strings = ['aba', 'xyz', 'abc', '121']
count = 0

for string in strings:
    if string[0] == string[-1]:
        count += 1

print("문자열의 개수 =", count)