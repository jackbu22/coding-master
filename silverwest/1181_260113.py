# n = int(input())

# strs = [str(input()) for i in range(n)]

# strs = list(set(strs))
# strs.sort()
# strs.sort(key=len)

# for str in strs:
#     print(str)


n = int(input())

for i in range(1, n + 1):
    print('*' * i)