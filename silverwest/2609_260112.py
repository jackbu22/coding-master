nums = list(map(int, input().split()))
nums.sort()

a = nums[0]
b = nums[1]

x = 1


for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        x = i

y = int(x * (a / x) * (b / x))

print(x)
print(y)
        

