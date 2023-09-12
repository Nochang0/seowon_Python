# 202311420 연승현
# 248P 11번

def deci2bin(n):
    if n == 0:
        return '0'
    binary_str = ''
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2
    return binary_str

decimal = 32
binary = deci2bin(decimal)
print(f"10진수: {decimal}")
print(binary)