# import sys
# input= sys.stdin.readline

# number=int(input())
# numbers=[]
# for i in range(1,number+1):
#     numbers.append(i)
# print(numbers)

# while len(numbers)!=1:
#     numbers.pop(0)
#     if len(numbers)!=1:
#         numbers.append(numbers.pop(0))

# print(numbers[0])

from collections import deque
import sys
input= sys.stdin.readline

number=int(input())
numbers=deque()

for i in range(1,number+1):
    numbers.append(i)
# print(numbers)
while len(numbers)!=1:
    numbers.popleft()
    if len(numbers)!=1:
        numbers.append(numbers.popleft())

print(numbers[0])
