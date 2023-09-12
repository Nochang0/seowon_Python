password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
print("로그인 성공")

adj = ["small", "medium", "large"]
nouns = ["apple", "banana", "grape"]

for x in adj:
  for y in nouns:
    print(x, y)