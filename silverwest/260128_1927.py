# import sys
# input = sys.stdin.readline

# n = int(input())

# array = []

# for _ in range(n):
#     comm = int(input())
#     if comm == 0 :
#         if len(array) > 0:
#             print(array[-1])
#             array.pop()
#         else:
#             print(0)
        
#     else:
#         array.append(comm)
#         if len(array)> 1 :
#             for i in range(1, len(array)):
#                 if array[i-1] < array[i]:
#                     array[i - 1], array[i] = array[i], array[i - 1]
#         else:
#             continue

l = [1,2,3,4]
print(min(l))