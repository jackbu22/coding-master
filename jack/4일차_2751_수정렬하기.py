import sys

input= sys.stdin.readline

count=int(input().strip())
# print(count)

numbers=[]

for i in range(count):
    number=int(input().strip())
    numbers.append(number)

# print(numbers)

numbers.sort()

# print(numbers)

for i in numbers:
    print(i)