# 301P

# 15

import random
list = []
for i in range(10):
    a = random.randint(0, 1)
    list.append(a)
print(list)
def find_longest_consecutive_sequence(arr):
    max_length = 0  
    current_length = 1 
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_length += 1
        else:
            current_length = 1  
        
        if current_length > max_length:
            max_length = current_length
    
    return max_length

result = find_longest_consecutive_sequence(list)
print(f"최대 연속 길이: {result}")