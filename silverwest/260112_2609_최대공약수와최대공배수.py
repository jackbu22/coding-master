#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

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
        

